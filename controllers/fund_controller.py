from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import fund_service
from models.fund_schema import FundPostSchema, FundSchema

router = APIRouter()

@router.get("/get-all-funds")
def get_all():
    results = fund_service.get_all_funds()
    return results

@router.get("/get-all-direct-family-funds")
def get_all():
    results = fund_service.get_all_direct_family_funds()
    return results


@router.get("/get-fund-by-id/{id}")
async def get_by_id(id: int):

    fund = fund_service.get_fund_with_id(id)
    if fund is None:
        raise HTTPException(status_code=404, detail="")
    return fund

@router.get("/get-fund-by-name/{name}")
async def get_by_name(name: str):

    fund = fund_service.get_fund_with_name(name)
    if fund is None:
        raise HTTPException(status_code=404, detail="")
    return fund

@router.get("/get-fund-allocation/{id}")
async def get_fund_allocation(id: int):

    fund = fund_service.get_fund_allocation(id)
    if fund is None:
        raise HTTPException(status_code=404, detail="")
    return fund


@router.post("/add-fund")
async def add_fund(new_fund: FundPostSchema=Body(...)):

    fund =  fund_service.create_new_fund(new_fund)
    if fund is None:
        raise HTTPException(status_code=404, detail="")
    return fund

@router.put("/update-fund/{id}")
async def update_fund(id: int, update: FundSchema=Body(...)):

    fund =  fund_service.update_fund(id, update)
    if fund is None:
        raise HTTPException(status_code=404, detail="")
    return fund

@router.delete("/delete-fund/{id}")
async def update_fund(id: int):

    return fund_service.delete_fund(id)