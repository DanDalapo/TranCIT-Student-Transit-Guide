

from django.contrib import admin
from .models import Route, SavedRoute, Landmark, JeepneyRoute, RouteStop, FareConfig


admin.site.register(Route)

class RouteStopInline(admin.TabularInline):
    model = RouteStop
    extra = 1  
    ordering = ('order',)  
    autocomplete_fields = ['landmark']  

@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name',)  

@admin.register(JeepneyRoute)
class JeepneyRouteAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')
    search_fields = ('code', 'description')
    inlines = [RouteStopInline] 

@admin.register(SavedRoute)
class SavedRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'origin', 'destination', 'transport_type', 'saved_at')

@admin.register(FareConfig)
class FareConfigAdmin(admin.ModelAdmin):
    list_display = ('transport_type', 'base_fare', 'initial_distance_km', 'extra_km_rate')

