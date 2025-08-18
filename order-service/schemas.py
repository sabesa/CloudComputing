from pydantic import BaseModel
from typing import List, Any

class Item(BaseModel):
    game_id: int
    title: str
    price: float

class OrderCreate(BaseModel):
    customer_name: str
    total_price: float
    items: List[Item]

class OrderRead(OrderCreate):
    id: int

    class Config:
        from_attributes = True