import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

shema = graphene.Schema(query=Query)
    # def resolve_hello(self, info, name):
    #     return f"Hello {name}"