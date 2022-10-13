
from pydantic import BaseModel

class OrderItemsSchema(BaseModel):
    product_code: str
    quantity: int = 0
    cartId: object 