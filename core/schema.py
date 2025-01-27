import graphene
from graphene_django import DjangoObjectType
from metrobus.models import Trip, StopTime, Shape

class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = "__all__"

class TripType(DjangoObjectType):
    class Meta:
        model = Trip
        fields = "__all__"

class StopTimeType(DjangoObjectType):
    class Meta:
        model = StopTime
        fields = "__all__"

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    shapes = graphene.List(ShapeType)
    trips = graphene.List(TripType)
    stoptimes = graphene.List(StopTimeType)

    def resolve_hello(self, info, name):
        return f"Hello {name}"
    
    def resolve_shapes(self, info):
        return Shape.objects.all()
    
    def resolve_trips(self, info):
        return Trip.objects.all()
    
    def resolve_stoptimes(self, info):
        return StopTime.objects.all()
    
schema = graphene.Schema(query=Query)
    # def resolve_hello(self, info, name):
    #     return f"Hello {name}"