from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class GameAnalytics(Base):
    __tablename__ = "game_analytics"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer)
    game_title = Column(String)
    event_type = Column(String)
    event_value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)