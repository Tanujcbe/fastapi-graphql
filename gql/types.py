import strawberry

@strawberry.type
class User:
    id: int
    name: str
    email: str
    age: int
    country: str
    is_married: bool