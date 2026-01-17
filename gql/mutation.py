import strawberry
from mock_db import users

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, 
    name: str, 
    email: str,
    age: int,
    country: str, 
    is_married: bool
    ) -> bool :
        new_id = len(users) + 1
        new_user = {
            "id": new_id,
            "name": name,
            "email": email,
            "age": age,
            "country": country,
            "is_married": is_married
        }
        users.append(new_user)
        print(users)
        return True