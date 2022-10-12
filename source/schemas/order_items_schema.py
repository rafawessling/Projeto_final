import datetime
from typing import Optional
from pydantic import BaseModel, Field

from schemas.product_schema import ProductSchema
# from schemas.address_schema import Address
# from schemas.user_schema import UserSchema

class OrderItemsSchema(BaseModel):
    product_code: str
    quantity: int = 0