import datetime
from typing import List
from pydantic import BaseModel, Field
from schemas.order_items_schema import OrderItemsSchema


class OrderSchema(BaseModel):
    userId: object = Field(..., description="Id do usuário")
    order_item: List[OrderItemsSchema] = []
    price: float = Field(..., description="Preço total do pedido")
    paid: bool = Field(default=False, description="Se o pagamento foi efetuado")
    created: datetime.datetime = Field(default=datetime.datetime.now(), description="Data de criação do pedido")
    addressId: object = Field(..., description="Id do endereço")

    class Config:
        schema_extra = {
            "example": {
                "userId": "634dd501b6101538bd964b0d",
                "order_item": [],
                "price": 0,
                "paid": False,
                "created": datetime.datetime.now(),
                "addressId": "634dd520b6101538bd964b10"
            }
        }
