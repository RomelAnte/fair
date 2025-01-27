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

def deleteLocation(request, id):
    location = Location.objects.get(id=id)
    location.delete()
    
    return redirect('location')

def listSpace(request):
    spaces = Space.objects.all()
    return render(request, 'Spaces/index.html', {'spaces': spaces})

def spaceNew(request):
    locations = Location.objects.all()
    return render(request, 'Spaces/newSpace.html', {'locations': locations})

def saveSpace(request):
    name = request.POST.get('name')
    capacity = request.POST.get('capacity')
    loc = request.POST.get('location')
    location = Location.objects.get(id=loc)
    
    space = Space.objects.create(name=name, capacity=capacity, location=location)
    
    return redirect('listSpace')

def listSpaceForId(request, id):
    space = Space.objects.get(id=id)
    locations = Location.objects.all()
    return render(request, 'Spaces/updateSpace.html', {'space': space, 'locations': locations})

def updateSpace(request):
    id = request.POST.get('id')
    space = Space.objects.get(id=id)
    space.name = request.POST.get('name')
    space.capacity = request.POST.get('capacity')
    space.location = Location.objects.get(id=request.POST.get('location'))
    
    space.save()
    return redirect('listSpace')

def deleteSpace(request, id):
    space = Space.objects.get(id=id)
    space.delete()
    
    return redirect('listSpace')

def listExhibitor(request):
    exhibitors = Exhibitor.objects.all()
    return render(request, 'Exhibitors/index.html', {'exhibitors': exhibitors})

def exhibitorNew(request):
    spaces = Space.objects.all()
    return render(request, 'Exhibitors/newExhibitor.html', {'spaces': spaces})

def saveExhibitor(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    spa= request.POST.get('space')
    space = Space.objects.get(id=spa)
    
    exhibitor = Exhibitor.objects.create(name=name, email=email, phone=phone, space=space)
    
    return redirect('listExhibitor')
    


    



    
    
    

