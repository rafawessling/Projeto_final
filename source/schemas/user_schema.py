
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(..., min_length=3, description="Nome completo")
    email: EmailStr = Field(..., unique=True, description="E-mail")
    password: str = Field(..., min_length=8, description="Senha")
    _id: object

    class Config:
        schema_extra = {
            "example": {
                "name": "Luiza da Silva",
                "email": "luiza_silva@gmail.com",
                "password": "senhasecreta123"
            }
        }
