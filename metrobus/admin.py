from django.contrib import admin
from .models import Service, Route, Stop, Shape, Trip

# Register your models here.
admin.site.register(Service)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Shape)
admin.site.register(Trip)