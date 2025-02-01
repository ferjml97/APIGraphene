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
        fields = ("trip_id", "trip_headsign", "route", "service", "shape")

class StopTimeType(DjangoObjectType):
    class Meta:
        model = StopTime
        fields = ("arrival_time", "stop_sequence", "trip", "departure_time")

class SearchResults(graphene.Union):
    class Meta:
        types = (RouteType, StopType)

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    services = graphene.List(lambda: ServiceType, limit=graphene.Int())
    routes = graphene.List(lambda: RouteType, limit=graphene.Int())
    stops = graphene.List(lambda: StopType, limit=graphene.Int())
    shapes = graphene.List(lambda: ShapeType, limit=graphene.Int())
    trips = graphene.List(lambda: TripType, limit=graphene.Int())
    stoptimes = graphene.List(lambda: StopTimeType, limit=graphene.Int())
    search = graphene.List(SearchResults, )


    def resolve_search(self, info):
        qroutes = Route.objects.all()
        qstops = Stop.objects.all()
        return list(qroutes) + list(qstops)

    def resolve_hello(self, info, name):
        return f"Hello {name}"
    
    def resolve_services(self, info, limit=None):
        query = Service.objects.all()
        if limit:
            return query[:limit]
        return Service.objects.all()
    
    def resolve_routes(self, info, limit=None):
        query = Route.objects.all()
        if limit:
            return query[:limit]
        return Route.objects.all()
    
    def resolve_stops(self, info, limit=None):
        query = Stop.objects.all()
        if limit:
            return query[:limit]
        return Stop.objects.all()
    
    def resolve_shapes(self, info, limit=None):
        query = Shape.objects.all()
        if limit:
            return query[:limit]
        return Shape.objects.all()
    
    def resolve_trips(self, info, limit=None):
        query = Trip.objects.all()
        if limit:
            return query[:limit]
        return Trip.objects.all()
    
    def resolve_stoptimes(self, info, limit=None):
        query = StopTime.objects.all()
        if limit:
            return query[:limit]
        return StopTime.objects.all()
    
schema = graphene.Schema(query=Query)