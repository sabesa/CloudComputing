from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import GameAnalytics
from database import SessionLocal
from schemas import GameAnalyticsCreate, GameAnalyticsRead
from typing import List

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[GameAnalyticsRead])
def get_all_analytics(db: Session = Depends(get_db)):
    return db.query(GameAnalytics).all()

@router.post("/", response_model=GameAnalyticsRead)
def create_analytics(data: GameAnalyticsCreate, db: Session = Depends(get_db)):
    record = GameAnalytics(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/game/{game_id}", response_model=List[GameAnalyticsRead])
def get_analytics_for_game(game_id: int, db: Session = Depends(get_db)):
    return db.query(GameAnalytics).filter(GameAnalytics.game_id == game_id).all()