import strawberry
from mock_db import users
from gql.types import User
from strawberry.types import Info

def extract_fields(fields):
    result = {}
    for field in fields:
        if field.selections:
            result[field.name] = extract_fields(field.selections)
        else:
            result[field.name] = {}
    return result

@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self)->str:
        return "Hellow World"
    
    @strawberry.field
    def users(self, info: Info, limit: int=10, offset: int=0)->list[User]:
        requested_fields = extract_fields(info.selected_fields)
        print(requested_fields)
        user_list = users[offset:offset+limit] 
        return [User(**user)  for user in user_list]
    
    @strawberry.field
    def user(self, id:int)->User:
        return User(**users[id-1])