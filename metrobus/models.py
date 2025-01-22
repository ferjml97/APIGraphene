from django.db import models

# Create your models here.
class Viaje(models.Model):
    trip_id = models.CharField(max_length=50)
    service_id = models.CharField(max_length=50)
    route_id = models.CharField(max_length=50)
    trip_headsign = models.CharField(max_length=50)
    shape_id = models.CharField(max_length=50)

    def __str__(self):
        return self.trip_id
    