import datetime
from typing import Optional
from pydantic import BaseModel, Field

from source.schemas.product_schema import ProductSchema
# from source.schemas.address_schema import Address
# from source.schemas.user_schema import UserSchema

class OrderItemsSchema(BaseModel):
    product_code: str
    quantity: int = 0