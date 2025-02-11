from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import allocation_service
from models.allocation_schema import AllocationSchema

router = APIRouter()

@router.get("/get-all-allocations")
def get_all():  
    results = allocation_service.get_all_allocations()
    return results


@router.get("/get-allocation-by-id/{id}")
async def get_by_id(id: int):

    allocation = allocation_service.get_allocation_with_id(id)
    if allocation is None:
        raise HTTPException(status_code=404, detail="")
    return allocation

@router.get("/get-allocation-by-name/{name}")
async def get_by_name(name: str):

    allocation = allocation_service.get_allocation_with_name(name)
    if allocation is None:
        raise HTTPException(status_code=404, detail="")
    return allocation

@router.post("/add-allocation")
async def add_allocation(new_allocation: AllocationSchema=Body(...)):

    allocation =  allocation_service.create_new_allocation(new_allocation)
    if allocation is None:
        raise HTTPException(status_code=404, detail="")
    return allocation

@router.put("/update-allocation/{id}")
async def update_allocation(id: int, update: AllocationSchema=Body(...)):

    allocation =  allocation_service.update_allocation(id, update)
    if allocation is None:
        raise HTTPException(status_code=404, detail="")
    return allocation

@router.delete("/delete-allocation/{id}")
async def update_allocation(id: int):
    return allocation_service.delete_allocation(id)