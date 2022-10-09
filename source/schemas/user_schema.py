from pydantic import BaseModel, Field, EmailStr
from typing import Optional
class UserSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Nome completo")
    email: EmailStr = Field(..., unique=True, description="E-mail")
    password: str = Field(..., min_length=8, max_length=20, description="Senha")
    adress: str = Field(..., min_length=5, max_length=50, description="Endereço")

class User(UserSchema):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

class UpdateUser(BaseModel):
    name: Optional [str] = Field(..., min_length=3, max_length=100, description="Novo nome completo")
    email: Optional [EmailStr] = Field(..., unique=True, description="Novo e-mail")
    password: Optional [str] = Field(..., min_length=8, max_length=20, description="Nova senha")
    adress: Optional [str] = Field(..., min_length=5, max_length=50, description="Novo endereço")