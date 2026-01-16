from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry


app = FastAPI(
    title="FastAPI App",
    description="A simple FastAPI application",
    version="1.0.0"
)



@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self)->str:
        return "Hellow World"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)


app.include_router(graphql_app, prefix="/graphql")