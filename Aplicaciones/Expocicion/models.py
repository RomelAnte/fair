from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    longitude = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Space(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exhibitor(models.Model):    
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
