import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from source.schemas.order_items_schema import OrderItemsSchema
# from source.schemas.address_schema import Address
# from source.schemas.user_schema import UserSchema

class OrderSchema(BaseModel):
    user: str
    order_item: List[OrderItemsSchema] = []
    price: float = Field(...)
    paid: bool = Field(default=False)
    created: datetime.datetime = Field(default=datetime.datetime.now())
    address: str