from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='routes_page'),
    path('plan_route/', views.plan_route, name='plan_route'),
    path('get_route_data/', views.get_route_data, name='get_route_data'),
    path('suggest_route/', views.suggest_route, name='suggest_route'),
    path('save_current_route/', views.save_current_route, name='save_current_route'),
    path('save_suggested_route/', views.save_suggested_route, name='save_suggested_route'),
    path('delete_saved_route/', views.delete_saved_route, name='delete_saved_route'),
    
    path('logout/', views.logout_view, name='logout'),
]