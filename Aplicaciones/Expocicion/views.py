from django.shortcuts import render, redirect
from .models import Location, Space, Exhibitor

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def listLocation(request):
    locations = Location.objects.all()
    return render(request, 'Locations/index.html', {'locations': locations})

def locationNew(request):
    return render(request, 'Locations/newLocation.html')

def newLocation(request):
    name = request.POST.get('name')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    city = request.POST.get('city')
    
    location = Location.objects.create(name=name, latitude=latitude, longitude=longitude, city=city)
    location.save()
    return redirect('location')

def listLocationForId(request, id):
    locations = Location.objects.get(id=id)
    return render(request, 'Locations/updateLocation.html', {'locations': locations})

def update_location(request):
    id = request.POST.get('id')
    
    location = Location.objects.get(id=id)
    location.id = id
    location.name = request.POST.get('name')
    location.latitude = request.POST.get('latitude')
    location.longitude = request.POST.get('longitude')
    location.city = request.POST.get('city')
    
    location.save()
    return redirect('location')

    
    
    

