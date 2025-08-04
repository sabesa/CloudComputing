from fastapi import FastAPI
import game
from database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Game Service API")

# Include game routes
app.include_router(game.router)
