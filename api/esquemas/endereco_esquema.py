from typing import List
from pydantic import BaseModel, Field




class Address(BaseModel):
    rua: str = Field(...)
    num: int = Field(...)
    cep: str = Field(..., unique=True)
    cidade: str = Field(...)
    estado: str = Field(...)


class Address_user(BaseModel):
    ...