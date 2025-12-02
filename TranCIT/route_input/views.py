# --- START OF FILE: route_input/views.py ---

from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache
from django.conf import settings
from django.db import DatabaseError
from django.db.models import Q
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.utils import timezone
from decimal import Decimal, InvalidOperation
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import openrouteservice
import json
import logging
import folium

# --- (1/2) MODIFICATION: IMPORT ceil ---
from math import ceil
# --- END MODIFICATION ---

from django.urls import reverse

from .forms import RouteForm, JeepneySuggestionForm
from .models import Route, SavedRoute, JEEPNEY_CODE_CHOICES
from .jeepney_data import JEEPNEY_ROUTES, LANDMARKS


# -----------------------------
# Configuration / Constants
# -----------------------------
logger = logging.getLogger(__name__)

# Cities for Cebu-area heuristics
CEBU_CITY_KEYWORDS = ["cebu", "mandaue", "lapu", "liloan", "consolacion", "talisay"]

# Default map center (put in settings if you prefer)
DEFAULT_MAP_CENTER = getattr(settings, 'DEFAULT_MAP_CENTER', (10.3157, 123.8854))
DEFAULT_MAP_ZOOM = getattr(settings, 'DEFAULT_MAP_ZOOM', 15)

# Cache timeouts (seconds)
GEOCODE_CACHE_TTL = getattr(settings, 'GEOCODE_CACHE_TTL', 24 * 60 * 60)  # 24 hours
ORS_ROUTE_CACHE_TTL = getattr(settings, 'ORS_ROUTE_CACHE_TTL', 6 * 60 * 60)  # 6 hours
MAP_HTML_CACHE_TTL = getattr(settings, 'MAP_HTML_CACHE_TTL', 5 * 60)  # 5 minutes

# Init geolocator
geolocator = Nominatim(user_agent=getattr(settings, 'GEOCODER_USER_AGENT', 'trancit_app_geocoder'))

# Initialize ORS client (may raise if not configured)
ORS_API_KEY = getattr(settings, 'ORS_API_KEY', None)
if ORS_API_KEY:
    ors_client = openrouteservice.Client(key=ORS_API_KEY)
else:
    ors_client = None


# -----------------------------
# Helper functions
# -----------------------------

def _cache_key_for_geocode(address: str) -> str:
    return f"geo:{address.strip().lower()}"


def cached_geocode(address: str):
    """Geocode with caching and fallback heuristics. Returns geopy Location or None."""
    if not address:
        return None

    key = _cache_key_for_geocode(address)
    cached = cache.get(key)
    if cached:
        return cached

    # Try a few fallbacks, similar to your safe_geocode
    query = address.strip()
    lower = query.lower()
    try:
        if not any(city in lower for city in CEBU_CITY_KEYWORDS):
            query_with_context = f"{query}, Cebu, Philippines"
        else:
            query_with_context = query

        location = geolocator.geocode(query_with_context, timeout=7)
        if not location:
            query_no_numbers = " ".join([w for w in query_with_context.split() if not w.isdigit()])
            location = geolocator.geocode(query_no_numbers, timeout=7)
        if not location:
            parts = [p.strip() for p in query.split(",") if p.strip()]
            if len(parts) >= 2:
                simplified = ", ".join(parts[:2]) + ", Cebu, Philippines"
                location = geolocator.geocode(simplified, timeout=7)
        if not location:
            # city-level fallback
            if "lapu" in lower:
                location = geolocator.geocode("Lapu-Lapu City, Cebu, Philippines", timeout=7)
            elif "mandaue" in lower:
                location = geolocator.geocode("Mandaue City, Cebu, Philippines", timeout=7)
            else:
                location = geolocator.geocode("Cebu City, Philippines", timeout=7)

        if location:
            # store a small tuple to avoid pickling geopy objects
            cached_val = (location.latitude, location.longitude, getattr(location, 'address', None))
            cache.set(key, cached_val, GEOCODE_CACHE_TTL)
            return cached_val

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        logger.warning("Geocoder error for %s: %s", address, e, exc_info=True)

    return None


def _parse_decimal(value):
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return None


def calculate_distance_and_time(start_lat, start_lon, end_lat, end_lon):
    """Approximate (geodesic) distance and a naive travel time estimate."""
    if not all([start_lat, start_lon, end_lat, end_lon]):
        return None, None

    try:
        coords_1 = (float(start_lat), float(start_lon))
        coords_2 = (float(end_lat), float(end_lon))
        distance_km = geodesic(coords_1, coords_2).km
        # conservative average speed assumption (kph)
        average_speed_kph = 20
        travel_time_minutes = (distance_km / average_speed_kph) * 60
        return Decimal(f"{distance_km:.2f}"), Decimal(f"{travel_time_minutes:.2f}")
    except Exception:
        logger.exception("Failed to calculate geodesic distance")
        return None, None


def calculate_fare(transport_type, distance_km, travel_time_minutes):
    """
    Calculates the estimated fare based on the transport type and distance,
    using the logic provided for Cebu's transport system.
    """
    if distance_km is None:
        return None
    
    try:
        distance = Decimal(distance_km)
        # Use a default of 0 for travel time if not provided
        waiting_time = Decimal(travel_time_minutes or 0)
        fare = Decimal('0.00')

        if transport_type == 'Jeepney':
            base = Decimal('13.00') # 
            rate = Decimal('1.80') # 
            if distance <= 4:
                fare = base
            else:
                fare = base + (distance - 4) * rate
        
        elif transport_type == 'Bus':
            base = Decimal('15.00') # 
            rate = Decimal('1.80') # 
            if distance <= 4:
                fare = base
            else:
                fare = base + (distance - 4) * rate

        elif transport_type == 'Taxi':
            base = Decimal('50.00') # 
            rate_km = Decimal('13.50') # 
            rate_waiting = Decimal('2.00') # 
            fare = base + (distance * rate_km) + (waiting_time * rate_waiting)

        elif transport_type == 'Motorcycle':
            # No official PDF provided, using existing logic from your code
            base = Decimal('20.00')
            if distance <= 1:
                fare = base
            elif distance <= 8:
                fare = base + (distance - 1) * Decimal('16.00')
            else:
                # Fare for first 8km + fare for remaining distance
                fare = base + (Decimal('7') * Decimal('16.00')) + (distance - 8) * Decimal('20.00')

        # --- (2/2) MODIFICATION: Round the final fare UP ---
        # Convert the Decimal to a float, apply ceiling to round up, then format back to a Decimal
        final_fare = ceil(float(fare))
        return Decimal(f"{final_fare:.2f}")
        # --- END MODIFICATION ---

    except Exception:
        logger.exception("Fare calculation failed")
        return None


def _ors_cache_key(a_lat, a_lon, b_lat, b_lon, profile):
    return f"ors:{float(a_lat):.6f},{float(a_lon):.6f}:{float(b_lat):.6f},{float(b_lon):.6f}:{profile}"


def get_route_geojson_cached(start_lat, start_lon, end_lat, end_lon, profile='driving-car'):
    """Fetch a geojson route from ORS with caching. Returns the geojson (dict) or None."""
    if ors_client is None:
        logger.warning("ORS client not configured (no API key)")
        return None

    key = _ors_cache_key(start_lat, start_lon, end_lat, end_lon, profile)
    cached = cache.get(key)
    if cached:
        return cached

    try:
        coords = [(float(start_lon), float(start_lat)), (float(end_lon), float(end_lat))]
        route = ors_client.directions(coordinates=coords, profile=profile, format='geojson')
        cache.set(key, route, ORS_ROUTE_CACHE_TTL)
        return route
    except Exception as e:
        logger.exception("ORS route request failed: %s", e)
        return None


def get_route_and_calculate(start_lat, start_lon, end_lat, end_lon, transport_type='driving-car'):
    profile_map = {
        'Taxi': 'driving-car',
        'Motorcycle': 'driving-car',
        'Jeepney': 'driving-car',
        'Bus': 'driving-car',
    }
    profile = profile_map.get(transport_type, 'driving-car')
    route_data = get_route_geojson_cached(start_lat, start_lon, end_lat, end_lon, profile=profile)
    if not route_data or 'features' not in route_data or not route_data['features']:
        logger.warning("ORS returned no features for route %s -> %s", (start_lat, start_lon), (end_lat, end_lon))
        return None, None, None

    try:
        feature = route_data['features'][0]
        props = feature.get('properties', {})
        summary = props.get('summary', {})
        distance_m = summary.get('distance', 0)
        duration_s = summary.get('duration', 0)
        distance_km = Decimal(str(distance_m / 1000))
        travel_time_minutes = Decimal(str(duration_s / 60))
        return distance_km, travel_time_minutes, route_data
    except Exception:
        logger.exception("Failed to extract ORS summary")
        return None, None, None


def store_route_path(route_instance, route_geojson):
    """Store route path coordinates on the model instance (as JSON lat/lon list)."""
    if not route_geojson or 'features' not in route_geojson:
        return
    try:
        feature = route_geojson['features'][0]
        coords = feature.get('geometry', {}).get('coordinates', [])
        path_coords = [[float(lat), float(lon)] for lon, lat in coords]
        route_instance.route_path_coords = json.dumps(path_coords)
    except Exception:
        logger.exception("Failed storing route path")


# The @login_required decorator has been removed from this function
def index(request):
    """Main dashboard view. Builds the folium map and handles route calculation for display."""
    error_message = None
    success_message = None

    # Get search/filter parameters from GET request
    origin_q = request.GET.get('origin_search', '')
    dest_q = request.GET.get('destination_search', '')
    transport_q = request.GET.get('transport_type_search', '')
    code_q = request.GET.get('jeepney_code_search', '')

    # Filter suggested routes based on search parameters
    suggested_qs = Route.objects.all().order_by('transport_type', 'code', 'origin')
    filters = Q()
    if origin_q: filters &= Q(origin__icontains=origin_q)
    if dest_q: filters &= Q(destination__icontains=dest_q)
    if transport_q: filters &= Q(transport_type=transport_q)
    if code_q: filters &= Q(code=code_q)
    if filters: suggested_qs = suggested_qs.filter(filters)

    # Initialize forms
    form = RouteForm()
    suggestion_form = JeepneySuggestionForm()

    # Get current origin/destination data from GET request (from Navigate button or pins)
    get_origin_lat = request.GET.get('origin_latitude')
    get_origin_lon = request.GET.get('origin_longitude')
    get_origin_text = request.GET.get('origin_text')
    get_dest_lat = request.GET.get('destination_latitude')
    get_dest_lon = request.GET.get('destination_longitude')
    get_dest_text = request.GET.get('destination_text')

    current_origin_lat = _parse_decimal(get_origin_lat)
    current_origin_lon = _parse_decimal(get_origin_lon)
    current_dest_lat = _parse_decimal(get_dest_lat)
    current_dest_lon = _parse_decimal(get_dest_lon)
    
    # Determine map center
    if current_origin_lat and current_dest_lat:
        center_lat = (float(current_origin_lat) + float(current_dest_lat)) / 2
        center_lon = (float(current_origin_lon) + float(current_dest_lon)) / 2
    elif current_origin_lat:
        center_lat, center_lon = float(current_origin_lat), float(current_origin_lon)
    elif current_dest_lat:
        center_lat, center_lon = float(current_dest_lat), float(current_dest_lon)
    else:
        center_lat, center_lon = DEFAULT_MAP_CENTER

    # Initialize calculated values for context
    calculated_fare = None
    calculated_distance = None
    calculated_time = None
    
    # --- MODIFIED: ADDED zoom_control=False ---
    m = folium.Map(location=[center_lat, center_lon], zoom_start=DEFAULT_MAP_ZOOM, zoom_control=False)

    if current_origin_lat and current_origin_lon:
        folium.Marker([float(current_origin_lat), float(current_origin_lon)], popup=get_origin_text or "Origin", icon=folium.Icon(color='blue', icon='circle', prefix='fa')).add_to(m)

    if current_dest_lat and current_dest_lon:
        folium.Marker([float(current_dest_lat), float(current_dest_lon)], popup=get_dest_text or "Destination", icon=folium.Icon(color='red', icon='circle', prefix='fa')).add_to(m)

    # If both origin and destination are set, calculate route and fare
    if current_origin_lat and current_origin_lon and current_dest_lat and current_dest_lon:
        try:
            transport_type_for_route = request.GET.get('transport_type', 'Jeepney')
            
            distance_km, travel_minutes, route_geojson = get_route_and_calculate(
                current_origin_lat, current_origin_lon,
                current_dest_lat, current_dest_lon,
                transport_type_for_route
            )
            
            if distance_km is not None:
                calculated_distance = distance_km
                calculated_time = travel_minutes
                calculated_fare = calculate_fare(transport_type_for_route, distance_km, travel_minutes)

            if route_geojson and 'features' in route_geojson and route_geojson['features']:
                coords = route_geojson['features'][0]['geometry']['coordinates']
                path_coords = [[coord[1], coord[0]] for coord in coords]
                folium.PolyLine(path_coords, color="#2B86C3EE", weight=8, opacity=0.8, popup="Calculated Route").add_to(m)
            else:
                folium.PolyLine([[float(current_origin_lat), float(current_origin_lon)], [float(current_dest_lat), float(current_dest_lon)]], color="#FF0000", weight=3, opacity=0.7, popup="Approximate route (ORS failed)").add_to(m)
        except Exception as e:
            logger.error(f"Error drawing route on map: {e}")

    # # Draw suggested routes on the map
    # for route in suggested_qs[:100]:
    #     path_coords = route.get_path_coords()
    #     if path_coords:
    #         folium.PolyLine(path_coords, color='purple', weight=3, opacity=0.7, popup=f"{route.transport_type} {route.code or ''}").add_to(m)
    
    click_js = """
function initFoliumMap() {
  for (const key in window) {
    if (key.startsWith("map_") && window[key] instanceof L.Map) {
      window.map = window[key];
      console.log("✅ Folium map found inside iframe:", key);
      attachHandlers();
      return;
    }
  }
  setTimeout(initFoliumMap, 500);
}

function attachHandlers() {
  if (!window.map) return;
  window.mapClickMode = null;

  var originIcon = L.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'blue' });
  var destIcon = L.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'red' });

  // Listen for messages from the parent page
  window.addEventListener("message", function(event) {
    const data = event.data;
    if (data?.type === "SET_PIN_MODE") {
      window.mapClickMode = data.mode;
    }

    if (data?.type === "DRAW_PIN") {
        const { lat, lng, mode, label } = data;
        if (!lat || !lng || !mode) return;

        const markerKey = mode === "origin" ? "originMarker" : "destinationMarker";

        // Remove existing marker
        if (window[markerKey]) {
            try { window.map.removeLayer(window[markerKey]); } catch {}
        }
        
        // Select correct icon
        var iconToUse = (mode === "origin") ? originIcon : destIcon;

        // Add new marker with ICON
        window[markerKey] = L.marker([lat, lng], {icon: iconToUse}).addTo(window.map)
            .bindPopup(label || (mode + ": " + lat.toFixed(5) + ", " + lng.toFixed(5)))
            .openPopup();
        
        window.mapClickMode = null; 
    }

    if (data?.type === "CLEAR_PINS") {
        if (window["originMarker"]) {
            try { window.map.removeLayer(window["originMarker"]); } catch {}
        }
        if (window["destinationMarker"]) {
            try { window.map.removeLayer(window["destinationMarker"]); } catch {}
        }
    }
  });

  window.map.on("click", function(e) {
    if (!window.mapClickMode) return;
    const { lat, lng } = e.latlng;

    const markerKey = window.mapClickMode === "origin" ? "originMarker" : "destinationMarker";

    if (window[markerKey]) {
      try { window.map.removeLayer(window[markerKey]); } catch {}
    }

    var iconToUse = (window.mapClickMode === "origin") ? originIcon : destIcon;
    window[markerKey] = L.marker([lat, lng], {icon: iconToUse}).addTo(window.map);

    const latInput = parent.document.getElementById("id_" + window.mapClickMode + "_latitude");
    const lonInput = parent.document.getElementById("id_" + window.mapClickMode + "_longitude");
    const textInput = parent.document.querySelector("input[name='" + window.mapClickMode + "']");
    
    if (latInput && lonInput) {
      latInput.value = lat.toFixed(6);
      lonInput.value = lng.toFixed(6);
      fetch("https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + lat + "&lon=" + lng)
        .then(r => r.json())
        .then(d => { textInput.value = d.display_name || `${lat.toFixed(5)}, ${lng.toFixed(5)}`; })
        .catch(() => { textInput.value = `${lat.toFixed(5)}, ${lng.toFixed(5)}`; });
    }

    window.mapClickMode = null;
  });
}

initFoliumMap();
"""

    m.get_root().html.add_child(folium.Element(f"<script>{click_js}</script>"))
    map_html = m._repr_html_()

    # Get saved routes for the user or session
    saved_routes = []
    if request.user.is_authenticated:
        saved_routes = SavedRoute.objects.filter(user=request.user)

    context = {
        'form': form,
        'suggestion_form': suggestion_form,
        'map': map_html,
        'all_routes': suggested_qs,
        'saved_routes': saved_routes,
        'success_message': success_message,
        'error_message': error_message,
        'get_origin_text': get_origin_text,
        'get_destination_text': get_dest_text,
        'search_origin': origin_q,
        'search_destination': dest_q,
        'search_transport_type': transport_q,
        'search_jeepney_code': code_q,
        'calculated_fare': calculated_fare,
        'calculated_distance': calculated_distance,
        'calculated_time': calculated_time,
    }

    if request.session.get('newbie_mode', False):
        return render(request, 'route_input/newbie_index.html', context)
    else:
        return render(request, 'route_input/index.html', context)


def _get_coords_from_request_data(address_text):
    """Helper to geocode text from POST data, with fallback."""
    if not address_text:
        return None, None, "Address text was empty."
    
    # Try geocoding the full text
    geo_result = cached_geocode(address_text)
    if geo_result:
        # cached_geocode returns a tuple (lat, lon, address)
        return geo_result[0], geo_result[1], None
    
    # Fallback/Error
    logger.warning("Could not geocode address during POST: %s", address_text)
    return None, None, f"Could not find coordinates for: {address_text}. Please pin it on the map."


@require_POST
def plan_route(request):
    """Endpoint to handle route planning + saving. Expects CSRF token if called from JS."""
    form = RouteForm(request.POST)
    if not form.is_valid():
        return render(request, 'route_input/index.html', {'form': form, 'error_message': 'Please check your inputs.'})

    route_instance = form.save(commit=False)

    post_origin_lat = request.POST.get('origin_latitude')
    post_origin_lon = request.POST.get('origin_longitude')
    post_dest_lat = request.POST.get('destination_latitude')
    post_dest_lon = request.POST.get('destination_longitude')

    # --- FIX 1: Handle Origin Geocoding ---
    if post_origin_lat and post_origin_lon:
        route_instance.origin_latitude = _parse_decimal(post_origin_lat)
        route_instance.origin_longitude = _parse_decimal(post_origin_lon)
    else:
        location_data = cached_geocode(route_instance.origin)
        if location_data:
            route_instance.origin_latitude = Decimal(str(location_data[0]))
            route_instance.origin_longitude = Decimal(str(location_data[1]))
        else:
            return render(request, 'route_input/index.html', {
                'form': form, 
                'error_message': f'Could not find coordinates for origin: {route_instance.origin}'
            })

    # --- FIX 2: Handle Destination Geocoding (This was missing!) ---
    if post_dest_lat and post_dest_lon:
        route_instance.destination_latitude = _parse_decimal(post_dest_lat)
        route_instance.destination_longitude = _parse_decimal(post_dest_lon)
    else:
        location_data = cached_geocode(route_instance.destination)
        if location_data:
            route_instance.destination_latitude = Decimal(str(location_data[0]))
            route_instance.destination_longitude = Decimal(str(location_data[1]))
        else:
            return render(request, 'route_input/index.html', {
                'form': form, 
                'error_message': f'Could not find coordinates for destination: {route_instance.destination}'
            })

    if all([route_instance.origin_latitude, route_instance.destination_latitude]):
        distance_km, travel_minutes, route_geojson = get_route_and_calculate(
            route_instance.origin_latitude, route_instance.origin_longitude,
            route_instance.destination_latitude, route_instance.destination_longitude,
            route_instance.transport_type
        )
        if distance_km is not None:
            route_instance.distance_km = distance_km
            route_instance.travel_time_minutes = travel_minutes
            route_instance.fare = calculate_fare(route_instance.transport_type, distance_km, travel_minutes)
            store_route_path(route_instance, route_geojson)
        else:
            d_km, t_min = calculate_distance_and_time(route_instance.origin_latitude, route_instance.origin_longitude, route_instance.destination_latitude, route_instance.destination_longitude)
            route_instance.distance_km = d_km
            route_instance.travel_time_minutes = t_min
            route_instance.fare = calculate_fare(route_instance.transport_type, d_km, t_min)

    # --- THIS IS THE FIXED CODE ---
    if route_instance.transport_type != 'Jeepney':
        route_instance.code = None
    else:
        route_instance.code = request.POST.get('code')

    # The route is now calculated and stored in 'route_instance' in memory.
    # ... (comments) ...
    # This block is now UN-INDENTED and will run for ALL transport types
    base_url = reverse('routes_page')
    query_params = f"origin_latitude={route_instance.origin_latitude}&origin_longitude={route_instance.origin_longitude}&origin_text={route_instance.origin}&destination_latitude={route_instance.destination_latitude}&destination_longitude={route_instance.destination_longitude}&destination_text={route_instance.destination}&transport_type={route_instance.transport_type}"
    return redirect(f"{base_url}?{query_params}")

# --- THIS IS THE CORRECTED FUNCTION ---
@require_POST
@login_required
def suggest_route(request):
    form = JeepneySuggestionForm(request.POST)
    if not form.is_valid():
        # If form is invalid, we can't just render the simple page.
        # We must redirect back with an error flag, or (better)
        # just log the error and redirect. For simplicity, we'll redirect.
        # A full solution would use Django messages framework.
        logger.warning(f"Invalid suggest_route form submission: {form.errors}")
        return redirect('routes_page') # Redirect back

    # --- START NEW LOGIC ---
    route_instance = form.save(commit=False)
    
    # Manually set transport_type since it's not in the suggestion form
    route_instance.transport_type = 'Jeepney'

    # Geocode Origin
    origin_lat, origin_lon, err = _get_coords_from_request_data(route_instance.origin)
    if err:
        # We can't geocode the origin. We should stop here.
        # In a full app, you'd send an error message. For now, we'll log and redirect.
        logger.warning(f"Could not geocode suggested origin: {route_instance.origin}")
        return redirect('routes_page')
    route_instance.origin_latitude = origin_lat
    route_instance.origin_longitude = origin_lon

    # Geocode Destination
    dest_lat, dest_lon, err = _get_coords_from_request_data(route_instance.destination)
    if err:
        logger.warning(f"Could not geocode suggested destination: {route_instance.destination}")
        return redirect('routes_page')
    route_instance.destination_latitude = dest_lat
    route_instance.destination_longitude = dest_lon

    # Get route path and other details from ORS
    distance_km, travel_minutes, route_geojson = get_route_and_calculate(
        route_instance.origin_latitude, route_instance.origin_longitude,
        route_instance.destination_latitude, route_instance.destination_longitude,
        route_instance.transport_type
    )
    
    # Save the calculated details
    if distance_km is not None:
        route_instance.distance_km = distance_km
        route_instance.travel_time_minutes = travel_minutes
        route_instance.fare = calculate_fare(route_instance.transport_type, distance_km, travel_minutes)
        
    if route_geojson:
        store_route_path(route_instance, route_geojson)
    
    # Now, save the complete object to the database
    try:
        route_instance.save()
        logger.info(f"New suggested route saved: {route_instance.code} from {route_instance.origin} to {route_instance.destination}")
    except DatabaseError as e:
        logger.error(f"Database error saving suggested route: {e}")
        # We would handle this error more gracefully in a full app
    
    return redirect('routes_page')


# --- THIS IS THE FIXED FUNCTION ---
@require_POST
@login_required
def save_current_route(request):
    origin = request.POST.get('origin')
    destination = request.POST.get('destination')
    transport_type = request.POST.get('transport_type')
    code = request.POST.get('code')
    fare_val = request.POST.get('fare')
    notes = request.POST.get('notes')

    # --- (1) ADD THIS BLOCK TO RE-CALCULATE THE ROUTE ---
    # Recalculate the route to get path data
    _, _, route_geojson = get_route_and_calculate(
        _parse_decimal(request.POST.get('origin_latitude')),
        _parse_decimal(request.POST.get('origin_longitude')),
        _parse_decimal(request.POST.get('destination_latitude')),
        _parse_decimal(request.POST.get('destination_longitude')),
        transport_type
    )
    # --- END OF NEW BLOCK ---

    # Try to find a matching base route, but it's okay if it's not found
    route = Route.objects.filter(Q(origin=origin) & Q(destination=destination) & Q(transport_type=transport_type) & Q(code=code)).first()
    
    saved = SavedRoute.objects.create(
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key or _get_session_key(request),
        original_route=route,
        origin=origin,
        destination=destination,
        
        origin_latitude=_parse_decimal(request.POST.get('origin_latitude')),
        origin_longitude=_parse_decimal(request.POST.get('origin_longitude')),
        destination_latitude=_parse_decimal(request.POST.get('destination_latitude')),
        destination_longitude=_parse_decimal(request.POST.get('destination_longitude')),

        transport_type=transport_type,
        code=code,
        fare=_parse_decimal(fare_val or 0),
        notes=notes or ""
        # We do NOT add route_path_coords here
    )

    # --- (2) ADD THIS BLOCK TO STORE THE PATH ---
    # Now store the path on the new 'saved' instance we just created
    if route_geojson:
        store_route_path(saved, route_geojson) # This function works on SavedRoute objects too
        saved.save() # Commit the change to the database
    # --- END OF NEW BLOCK ---

    return JsonResponse({"message": "Route saved successfully!", "id": saved.id})



@require_POST
@login_required
def save_suggested_route(request):
    route_id = request.POST.get('route_id')
    if not route_id: return JsonResponse({'error': 'route_id required'}, status=400)
    try: route = Route.objects.get(pk=int(route_id))
    except Route.DoesNotExist: return JsonResponse({'error': 'Route not found'}, status=404)

    saved = SavedRoute.objects.create(
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key or _get_session_key(request),
        original_route=route,
        origin=route.origin,
        destination=route.destination,
        origin_latitude=route.origin_latitude,
        origin_longitude=route.origin_longitude,
        destination_latitude=route.destination_latitude,
        destination_longitude=route.destination_longitude,
        transport_type=route.transport_type,
        code=route.code,
        fare=route.fare or 0,
        notes=route.notes or "",
        route_path_coords=route.route_path_coords
    )
    return JsonResponse({"message": "Suggested route saved!", "id": saved.id})


@require_POST
@login_required
def delete_saved_route(request):
    saved_id = request.POST.get('saved_id')
    if not saved_id: return JsonResponse({'success': False, 'error': 'saved_id required.'}, status=400)
    try: saved = SavedRoute.objects.get(pk=int(saved_id))
    except (SavedRoute.DoesNotExist, ValueError): return JsonResponse({'success': False, 'error': 'Not found.'}, status=404)

    if (request.user.is_authenticated and saved.user != request.user) or \
       (not request.user.is_authenticated and saved.session_key != (request.session.session_key or _get_session_key(request))):
        return JsonResponse({'success': False, 'error': 'Forbidden.'}, status=403)

    saved.delete()
    return JsonResponse({'success': True})


@require_POST
def save_route_ajax(request):
    try:
        data = request.POST
        route = SavedRoute.objects.create(
            user=request.user if request.user.is_authenticated else None,
            origin=data.get('origin', ''),
            destination=data.get('destination', ''),
            origin_latitude=_parse_decimal(data.get('origin_latitude')),
            origin_longitude=_parse_decimal(data.get('origin_longitude')),
            destination_latitude=_parse_decimal(data.get('destination_latitude')),
            destination_longitude=_parse_decimal(data.get('destination_longitude')),
            transport_type=data.get('transport_type', 'Unknown'),
            code=data.get('code', ''),
            fare=_parse_decimal(data.get('fare') or 0)
        )
        return JsonResponse({'success': True, 'route': {'id': route.id, 'origin': route.origin, 'destination': route.destination, 'transport_type': route.transport_type, 'code': route.code, 'fare': float(route.fare or 0)}})
    except Exception as e:
        logger.exception("Error saving route via ajax")
        return JsonResponse({'success': False, 'error': str(e)})


@require_GET
def get_jeep_codes(request):
    return JsonResponse({'codes': [code for code, _ in JEEPNEY_CODE_CHOICES]})


def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


@require_POST
def get_route_data(request):
    try:
        data = json.loads(request.body)
        origin_lat = _parse_decimal(data.get('origin_latitude'))
        origin_lon = _parse_decimal(data.get('origin_longitude'))
        dest_lat = _parse_decimal(data.get('destination_latitude'))
        dest_lon = _parse_decimal(data.get('destination_longitude'))
        transport_type = data.get('transport_type', 'Jeepney')

        if not all([origin_lat, origin_lon, dest_lat, dest_lon]):
            return JsonResponse({'error': 'Missing coordinates.'}, status=400)

        # Calculate the route (this is the slow part)
        distance_km, travel_minutes, route_geojson = get_route_and_calculate(
            origin_lat, origin_lon, dest_lat, dest_lon, transport_type
        )

        if distance_km is None:
            return JsonResponse({'error': 'Could not calculate route.'}, status=500)

        # Calculate the fare
        fare = calculate_fare(transport_type, distance_km, travel_minutes)

        alternatives = []
        if transport_type == 'Jeepney':
            alternatives = find_best_jeepneys(origin_lat, origin_lon, dest_lat, dest_lon)

        # Get the raw path coordinates for the map
        path_coords = []
        if route_geojson and 'features' in route_geojson and route_geojson['features']:
            coords = route_geojson['features'][0]['geometry']['coordinates']
            path_coords = [[coord[1], coord[0]] for coord in coords]

        # Send all the data back to the JavaScript
        return JsonResponse({
            'success': True,
            'distance_km': float(distance_km),
            'travel_time_minutes': float(travel_minutes),
            'fare': float(fare),
            'path_coords': path_coords,
            'alternatives': alternatives
        })

    except Exception as e:
        logger.error(f"Error in get_route_data: {e}")
        return JsonResponse({'error': str(e)}, status=500)
    
# --- SMART SUGGESTION HELPERS ---

def get_nearby_routes(point, threshold_km=0.8):
    """
    Returns a list of routes within threshold_km of a point.
    Includes the distance to that point.
    """
    nearby_routes = []
    for code, data in JEEPNEY_ROUTES.items():
        best_stop = None
        best_dist = float('inf')
        best_coords = None

        for landmark in data['path']:
            coords = LANDMARKS.get(landmark)
            if coords:
                dist = geodesic(point, coords).km
                if dist <= threshold_km and dist < best_dist:
                    best_dist = dist
                    best_stop = landmark
                    best_coords = coords

        if best_stop:
            nearby_routes.append({
                'code': code,
                'stop': best_stop,
                'coords': best_coords,
                'dist_km': best_dist,
                'data': data
            })
    return nearby_routes

def find_best_jeepneys(origin_lat, origin_lon, dest_lat, dest_lon):
    """
    Finds Direct Routes AND 1-Transfer Routes.
    """
    suggestions = []
    user_origin = (origin_lat, origin_lon)
    user_dest = (dest_lat, dest_lon)

    routes_at_origin = get_nearby_routes(user_origin)
    routes_at_dest = get_nearby_routes(user_dest)
    route_paths_map = {r['code']: r['data']['path'] for r in routes_at_origin + routes_at_dest}

    # --- STRATEGY A: DIRECT ROUTES ---
    for start_r in routes_at_origin:
        for end_r in routes_at_dest:
            if start_r['code'] == end_r['code']:
                path = route_paths_map[start_r['code']]
                try:
                    start_idx = path.index(start_r['stop'])
                    end_idx = path.index(end_r['stop'])
                    if start_idx < end_idx:
                        suggestions.append({
                            'type': 'direct',
                            'code': start_r['code'],
                            'description': JEEPNEY_ROUTES[start_r['code']]['description'],
                            'board_at': start_r['stop'],
                            'alight_at': end_r['stop'],
                            'walk_dist': f"{start_r['dist_km']*1000:.0f}m",
                            'board_coords': start_r['coords'],
                            'alight_coords': end_r['coords'],
                            'origin_coords': user_origin,
                            'dest_coords': user_dest
                        })
                except ValueError: continue

    if len(suggestions) > 0: return suggestions[:3]

    # --- STRATEGY B: 1-TRANSFER ROUTES ---
    for start_r in routes_at_origin:
        for end_r in routes_at_dest:
            if start_r['code'] == end_r['code']: continue 

            path_a = JEEPNEY_ROUTES[start_r['code']]['path']
            path_b = JEEPNEY_ROUTES[end_r['code']]['path']
            common_stops = set(path_a).intersection(set(path_b))

            if common_stops:
                valid_transfer = None
                for stop in path_a:
                    if stop in common_stops:
                        try:
                            idx_board_a = path_a.index(start_r['stop'])
                            idx_transfer_a = path_a.index(stop)
                            idx_transfer_b = path_b.index(stop)
                            idx_drop_b = path_b.index(end_r['stop'])
                            if idx_board_a < idx_transfer_a and idx_transfer_b < idx_drop_b:
                                valid_transfer = stop
                                break
                        except ValueError: continue

                if valid_transfer:
                    suggestions.append({
                        'type': 'transfer',
                        'code_1': start_r['code'],
                        'code_2': end_r['code'],
                        'description': f"Transfer at {valid_transfer}",
                        'board_at': start_r['stop'],
                        'transfer_at': valid_transfer,
                        'alight_at': end_r['stop'],
                        'walk_dist': f"{start_r['dist_km']*1000:.0f}m",
                        'board_coords': start_r['coords'],
                        'transfer_coords': LANDMARKS.get(valid_transfer),
                        'alight_coords': end_r['coords'],
                        'origin_coords': user_origin,
                        'dest_coords': user_dest
                    })
                    if len(suggestions) >= 3: return suggestions

    return suggestions

@require_POST
def get_segment_path(request):
    """Calculates a path segment (walking or driving) for visualization."""
    try:
        data = json.loads(request.body)
        start = data.get('start')
        end = data.get('end')
        mode = data.get('mode')

        if not start or not end:
            return JsonResponse({'error': 'Missing coordinates'}, status=400)

        profile = 'foot-walking' if mode == 'walking' else 'driving-car'

        route_geojson = get_route_geojson_cached(
            start_lat=start[0], start_lon=start[1],
            end_lat=end[0], end_lon=end[1],
            profile=profile
        )

        path_coords = []
        if route_geojson and 'features' in route_geojson:
             coords = route_geojson['features'][0]['geometry']['coordinates']
             path_coords = [[c[1], c[0]] for c in coords]

        return JsonResponse({'path_coords': path_coords})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def logout_view(request):
    logout(request)
    return redirect('/')