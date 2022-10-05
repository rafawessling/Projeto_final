from pydantic import BaseModel, Field, EmailStr
class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Nome completo")
    email: EmailStr = Field(..., unique=True, description="E-mail")
    password: str = Field(..., min_length=8, max_length=20, description="Senha")
    adress: str = Field(..., min_length=5, max_length=50, description="Endereço")
    id: int 