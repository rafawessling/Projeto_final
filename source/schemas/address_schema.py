from typing import List
from pydantic import BaseModel, Field
from user_schema import User

class Address(BaseModel):
    street: str = Field(...)
    num: int = Field(...)
    cep: str = Field(..., unique=True)
    city: str = Field(...)
    state: str = Field(...)

class Address_user(BaseModel):
    user: User
    address: List[Address] = []