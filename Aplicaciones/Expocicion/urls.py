from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('location', views.listLocation, name='location'),
    path('locationNew', views.locationNew, name='locationNew'),
    path('newLocation', views.newLocation, name='newLocation'),
    path('listLocationForId/<id>', views.listLocationForId, name='listLocationForId'),
    path('update_location', views.update_location, name='update_location'),
]