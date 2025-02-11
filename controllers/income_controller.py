from typing import List

from fastapi import APIRouter, HTTPException, Depends, Body
from models.Income_schema import IncomeSchema, IncomeSchemaPost
from services import income_service
router = APIRouter()

@router.put("/update-income")
async def update_project(updates: IncomeSchema=Body(...)):

    incomes = income_service.update_income(updates)
    if incomes is None:
        raise HTTPException(status_code=404, detail="")
    return incomes

@router.post("/add-income")
async def add_income(new_income: IncomeSchemaPost=Body(...)):

    income =  income_service.create_new_income(new_income)
    if income is None:
        raise HTTPException(status_code=404, detail="")
    return income

@router.delete("/delete-income/{id}")
async def delete_income(id: int):
    return income_service.delete_income(id)