from typing import List
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str = Field(...)
    num: int = Field(...)
    cep: str = Field(..., unique=True)
    city: str = Field(...)
    state: str = Field(...)