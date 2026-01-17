import strawberry
from .queries import Query
from .mutation import Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
