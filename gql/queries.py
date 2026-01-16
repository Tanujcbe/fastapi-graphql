import strawberry
from mock_db import users
from gql.types import User

@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self)->str:
        return "Hellow World"
    
    @strawberry.field
    def users(self)->list[User]:
        return [User(**user)  for user in users]
    
    @strawberry.field
    def user(self, id:int)->User:
        return User(**users[id-1])