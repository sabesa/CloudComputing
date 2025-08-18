from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Game
from schemas import GameCreate, GameRead  # <-- Import Pydantic models
from typing import List

router = APIRouter(prefix="/games", tags=["Games"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[GameRead])
def get_games(db: Session = Depends(get_db)):
    return db.query(Game).all()

@router.get("/{game_id}", response_model=GameRead)
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.post("/", response_model=GameRead)
def create_game(game_data: GameCreate, db: Session = Depends(get_db)):
    game = Game(**game_data.dict())
    db.add(game)
    db.commit()
    db.refresh(game)
    return game
