from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import support_service
from models.support_schema import SupportSchema, BaseSupport

router = APIRouter()

@router.get("/get-all-supports")
def get_all():
    
    results = support_service.get_all_supports()
    return results


@router.get("/get-support-by-id/{id}")
async def get_by_id(id: int):

    support = support_service.get_support_with_id(id)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.get("/get-all-needy-supports/{id}")
async def get_by_needy_id(id: int):

    support = support_service.get_suppport_by_needy_id(id)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.get("/get-allocation-supported/{id}")
async def get_by_needy_id(id: int):

    support = support_service.get_suppport_by_allocation_id(id)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.get("/get-support-by-name/{name}")
async def get_by_name(name: str):

    support = support_service.get_support_with_name(name)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.post("/add-support")
async def add_support(new_support: BaseSupport=Body(...)):
    support =  support_service.create_new_support(new_support)
    if support =="Not enough amount in allocation":
        raise HTTPException(status_code=404, detail="אין מספיק פריטם לחלוקה")
    return support

@router.put("/update-support/{id}")
async def update_support(id: int, update: BaseSupport=Body(...)):

    support =  support_service.update_support(id, update)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.delete("/delete-support/{id}")
async def delete_support(id: int):

    return support_service.delete_support(id)