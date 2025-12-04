from django.core.management.base import BaseCommand
from route_input.models import Landmark, JeepneyRoute, RouteStop
from route_input.jeepney_data import LANDMARKS, JEEPNEY_ROUTES
import sys

class Command(BaseCommand):
    help = 'Imports Jeepney data from jeepney_data.py into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting import...")

        # 1. Import Landmarks
        landmark_cache = {} # Cache created objects to avoid DB hits
        created_count = 0
        
        for name, coords in LANDMARKS.items():
            lat, lon = coords
            landmark, created = Landmark.objects.get_or_create(
                name=name,
                defaults={'latitude': lat, 'longitude': lon}
            )
            landmark_cache[name] = landmark
            if created: created_count += 1
        
        self.stdout.write(f"✅ Processed {len(landmark_cache)} landmarks ({created_count} new).")

        # 2. Import Routes
        route_count = 0
        for code, data in JEEPNEY_ROUTES.items():
            route, created = JeepneyRoute.objects.get_or_create(
                code=code,
                defaults={'description': data['description']}
            )
            
            # Clear existing stops to avoid duplicates if re-running
            RouteStop.objects.filter(route=route).delete()

            # Create stops in order
            stops_to_create = []
            for index, stop_name in enumerate(data['path']):
                landmark = landmark_cache.get(stop_name)
                
                if not landmark:
                    self.stdout.write(self.style.WARNING(f"⚠️ Warning: Landmark '{stop_name}' in route {code} not found in LANDMARKS list."))
                    continue

                stops_to_create.append(RouteStop(
                    route=route,
                    landmark=landmark,
                    order=index
                ))
            
            RouteStop.objects.bulk_create(stops_to_create)
            route_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully imported {route_count} routes."))