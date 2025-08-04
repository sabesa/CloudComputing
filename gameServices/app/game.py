from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Game
from database import SessionLocal

router = APIRouter(prefix="/games", tags=["Games"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_games(db: Session = Depends(get_db)):
    return db.query(Game).all()

@router.get("/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.post("/")
def create_game(game: Game, db: Session = Depends(get_db)):
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

@router.put("/{game_id}")
def update_game(game_id: int, updated_game: Game, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    for attr, value in vars(updated_game).items():
        setattr(game, attr, value)
    db.commit()
    return game

@router.delete("/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return {"detail": "Deleted successfully"}
