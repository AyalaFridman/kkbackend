from typing import List

from fastapi import APIRouter, HTTPException, Depends, Body
from models.expense_schema import ExpenseSchema, ExpenseSchemaPost
from services import expense_service
router = APIRouter()

@router.put("/update-expenses")
async def update_expense(updates: List[ExpenseSchema]=Body(...)):

    expenses = expense_service.update_expense(updates)
    if expenses is None:
        raise HTTPException(status_code=404, detail="")
    return expenses

@router.post("/add-expense")
async def add_income(new_expense: ExpenseSchemaPost=Body(...)):

    expense =  expense_service.create_new_expense(new_expense)
    if expense is None:
        raise HTTPException(status_code=404, detail="")
    return expense

@router.delete("/delete-expense/{id}")
async def delete_expense(id: int):
    return expense_service.delete_expense(id)