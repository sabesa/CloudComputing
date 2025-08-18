from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Order
from database import SessionLocal
from schemas import OrderCreate, OrderRead
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[OrderRead])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/", response_model=OrderRead)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    order = Order(
        customer_name=order_data.customer_name,
        total_price=order_data.total_price,
        items=[item.dict() for item in order_data.items]
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"detail": "Deleted successfully"}