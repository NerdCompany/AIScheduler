from pydantic import Field, BaseModel


class User(BaseModel):
    name: str
    city: str = Field(alias="address.city")  # Flattened
    country: str = Field(alias="address.country")  # Flattened


data = {"name": "Alice", "address": {"city": "London", "country": "UK"}}
user = User(**data)
print(user)
