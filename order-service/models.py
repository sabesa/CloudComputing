from sqlalchemy import Column, Integer, String, Float, JSON
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    total_price = Column(Float)
    items = Column(JSON)  # JSON list of items in the order

