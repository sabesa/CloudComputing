from fastapi import FastAPI
import order
from database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service API")
app.include_router(order.router)