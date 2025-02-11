from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import payments_service
from models.payments_schema import PaymentsSchemaGet, BasePaymentsSchema

router = APIRouter()

@router.get("/get-all-ayments")
def get_all():
    
    return payments_service.get_all_payments()


@router.get("/get-payment-by-id/{id}")
async def get_by_id(id: int):

    payment = payments_service.get_payment_with_id(id)
    if payment is None:
        raise HTTPException(status_code=404, detail="")
    return payment


@router.post("/add-payment")
async def add_payment(new_payment: BasePaymentsSchema=Body(...)):

    payment =  payments_service.add_payment(new_payment)
    if payment is None:
        raise HTTPException(status_code=404, detail="")
    return payment




