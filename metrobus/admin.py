from django.contrib import admin
from .models import Trip, StopTime, Shape, Stop, Service, Route

# Register your models here.
admin.site.register(Service)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Shape)
admin.site.register(Trip)
admin.site.register(StopTime)