
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str = Field(..., min_length=3, max_length=80, description="Nome da rua")
    num: int = Field(..., ge=1, description="Número")
    cep: str = Field(..., min_length=9, max_length=9, description="CEP",)
    city: str = Field(..., min_length=3, max_length=20, description="Cidade")
    state: str = Field(..., min_length=3, max_length=20, description="Estado")
    userId: object
    
    class Config:
        schema_extra = {
            "example": {
                "street": "Rua das Flores",
                "num": 1234,
                "cep": "80123-100",
                "city": "São Paulo",
                "state": "São Paulo",
                "userId": "634dd501b6101538bd964b0d"
            }
        }
