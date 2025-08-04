from sqlalchemy import Column, Integer, String, Float
from database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    release_date = Column(String)
    price = Column(Float)