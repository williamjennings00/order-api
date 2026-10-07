from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.db import SessionLocal
from database.models import Order


router = APIRouter()


class OrderCreate(BaseModel):
    customer_name: str
    product: str
    quantity: int = Field(gt=0)
    price: float = Field(ge=0)
    status: str = "pending"


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/orders")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    order = Order(
        customer_name=order_data.customer_name,
        product=order_data.product,
        quantity=order_data.quantity,
        price=order_data.price,
        status=order_data.status
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order

@router.get("/orders")
def get_all_orders(db: Session = Depends(get_db)):
    statement = select(Order)
    orders = db.scalars(statement).all()
    return orders


@router.get("/orders/{order_id}")
def get_order(order_id: str, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order
