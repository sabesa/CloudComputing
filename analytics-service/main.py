from fastapi import FastAPI
from analytics import router
from database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Analytics Service API")
app.include_router(router)