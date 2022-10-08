from typing import List
from pydantic import BaseModel, Field, EmailStr
from schemas.address_schema import Address

class User(BaseModel):
    name: str = Field(..., min_length=3, description="Nome completo")
    email: EmailStr = Field(..., unique=True, description="E-mail")
    password: str = Field(..., min_length=8, description="Senha")
    address: List[Address]
    _id: int