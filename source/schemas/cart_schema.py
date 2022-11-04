
from pydantic import BaseModel, Field

class CartSchema(BaseModel):
    user_id: object = Field(..., description="Id do usuário")
    total_price: float = Field(..., description="Preço total")

    class Config:
        schema_extra = {
            "example": {
                "user_id": "634dd501b6101538bd964b0d",
                "total_price": 0
            }
        }