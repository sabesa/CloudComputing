from pydantic import BaseModel
from typing import Optional

class GameBase(BaseModel):
    name: str
    category: str
    release_date: str
    price: float

class GameCreate(GameBase):
    pass

class GameRead(GameBase):
    id: int

    class Config:
        orm_mode = True
