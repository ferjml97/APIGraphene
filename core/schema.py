import graphene
from graphene_django import DjangoObjectType
from metrobus.models import Trip, StopTime, Shape, Stop, Service, Route

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = "__all__"

class StopType(DjangoObjectType):
    class Meta:
        model = Stop
        fields = "__all__"

class RouteType(DjangoObjectType):
    class Meta:
        model = Route
        fields = "__all__"

class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = "__all__"

class TripType(DjangoObjectType):
    class Meta:
        model = Trip
        fields = ("trip_id", "trip_headsign", "stoptimes")

class StopTimeType(DjangoObjectType):
    class Meta:
        model = StopTime
        fields = ("arrival_time", "stop_sequence", "trip", "departure_time")

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    services = graphene.List(ServiceType)
    routes = graphene.List(RouteType)
    stops = graphene.List(StopType)
    shapes = graphene.List(ShapeType)
    trips = graphene.List(TripType)
    stoptimes = graphene.List(StopTimeType)

    def resolve_hello(self, info, name):
        return f"Hello {name}"
    
    def resolve_services(self, info):
        return Service.objects.all()
    
    def resolve_routes(self, info):
        return Route.objects.all()
    
    def resolve_stops(self, info):
        return Stop.objects.all()
    
    def resolve_shapes(self, info):
        return Shape.objects.all()
    
    def resolve_trips(self, info):
        return Trip.objects.all()
    
    def resolve_stoptimes(self, info):
        return StopTime.objects.all()
    
schema = graphene.Schema(query=Query)