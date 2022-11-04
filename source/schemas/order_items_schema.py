
from pydantic import BaseModel, Field

class OrderItemsSchema(BaseModel):
    product_code: str = Field(..., description="Código do produto")
    quantity: int = Field(..., ge=1, description="Quantidade de itens")
    cartId: object = Field(..., description="Id do cart")

    class Config:
        schema_extra = {
            "example": {
                "product_code": "123456",
                "quantity": "3",
                "cartId": "63653c06a83bfb51873d1669"
            }
        }
