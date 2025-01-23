from django.db import models

# Create your models here.

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=50)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.service_id
    
class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=50)
    agency_id = models.CharField(max_length=50)
    route_short_name = models.CharField(max_length=10)
    route_long_name = models.CharField(max_length=250)
    route_url = models.CharField(max_length=250)
    route_color = models.CharField(max_length=10)

    def __str__(self):
        return self.route_id

class Stop(models.Model):
    stop_id = models.AutoField(primary_key=True)
    stop = models.CharField(max_length=50)
    #stop_code = models.CharField(max_length=50)
    stop_name = models.CharField(max_length=250)
    #stop_desc = models.CharField(max_length=250)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()

    def __str__(self):
        return self.stop_id

class Shape(models.Model):
    shape_id = models.AutoField(primary_key=True)
    shape = models.CharField(max_length=50)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.IntegerField()

    def __str__(self):
        return self.shape_id

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    trip = models.CharField(max_length=50)
    #service_id = models.CharField(max_length=50)
    trip_headsign = models.CharField(max_length=50)
    shape_id = models.ForeignKey(Shape, on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_id
    
class StopTime(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop_id = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_sequence = models.IntegerField()

    def __str__(self):
        return self.trip_id