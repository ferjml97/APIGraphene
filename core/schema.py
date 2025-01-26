import graphene
from graphene_django import DjangoObjectType
from metrobus.models import Trip, StopTime

class TripType(DjangoObjectType):
    class Meta:
        model = Trip

class StopTimeType(DjangoObjectType):
    class Meta:
        model = StopTime

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    trips = graphene.List(TripType)
    stoptimes = graphene.List(StopTimeType)

    def resolve_hello(self, info, name):
        return f"Hello {name}"
    
    def resolve_trips(self, info):
        return Trip.objects.all()
    
    def resolve_stoptimes(self, info):
        return StopTime.objects.all()
    
shema = graphene.Schema(query=Query)
    # def resolve_hello(self, info, name):
    #     return f"Hello {name}"