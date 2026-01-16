import strawberry
from mock_db import users

@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self)->str:
        print([user["name"] for user in users])
        return "Hellow World"