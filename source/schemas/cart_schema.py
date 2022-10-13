
from pydantic import BaseModel

class CartSchema(BaseModel):
    user_id: object 
    total_price: float
    