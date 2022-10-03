from typing import List
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(...)
    email: str = Field(..., unique=True)
    password: str = Field(...)
    adress: str = Field(...)
    id: int 