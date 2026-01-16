from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from mock_db import users
from gql.schema import schema

app = FastAPI(
    title="FastAPI App",
    description="A simple FastAPI application",
)



@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


graphql_app = GraphQLRouter(schema)


app.include_router(graphql_app, prefix="/graphql")