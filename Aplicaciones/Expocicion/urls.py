from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('location/', views.listLocation, name='location'),
    path('locationNew/', views.locationNew, name='locationNew'),
    path('newLocation/', views.newLocation, name='newLocation'),
    path('listLocationForId/<id>/', views.listLocationForId, name='listLocationForId'),
    path('update_location/', views.update_location, name='update_location'),
    path('deleteLocation/<id>', views.deleteLocation , name='deleteLocation'), 
    
    path('listSpace/', views.listSpace, name='listSpace'),
    path('spaceNew', views.spaceNew, name='spaceNew'),
    path('saveSpace/', views.saveSpace, name='saveSpace'),
    path('listSpaceForId/<id>/', views.listSpaceForId, name='listSpaceForId'),
    path('updateSpace/', views.updateSpace, name='updateSpace'),
    path('deleteSpace/<id>', views.deleteSpace , name='deleteSpace'), 
    
    
    
    
]