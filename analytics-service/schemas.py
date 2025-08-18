from pydantic import BaseModel
from datetime import datetime

class GameAnalyticsCreate(BaseModel):
    game_id: int
    game_title: str
    event_type: str
    event_value: float

class GameAnalyticsRead(GameAnalyticsCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True