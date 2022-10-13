import datetime
from typing import List
from pydantic import BaseModel, Field
from schemas.order_items_schema import OrderItemsSchema


class OrderSchema(BaseModel):
    userId: object
    order_item: List[OrderItemsSchema] = []
    price: float = Field(...)
    paid: bool = Field(default=False)
    created: datetime.datetime = Field(default=datetime.datetime.now())
    addressId: object 
