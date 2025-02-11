from fastapi import APIRouter, HTTPException, Depends, Body
from models.schema import AccountSchema
from services import account_service
router = APIRouter()

@router.put("/update-account/{id}")
async def update_project(id: int, update: AccountSchema=Body(...)):
    account = account_service.update_account(id, update)
    if account is None:
        raise HTTPException(status_code=404, detail="")
    return account