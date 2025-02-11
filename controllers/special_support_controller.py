from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import special_support_service
from models.special_support_schema import SpecialSupportSchema, BaseSpecialSupportSchema

router = APIRouter()

@router.get("/get-all-special_supports")
def get_all():
    results = special_support_service.get_all_special_supports()
    return results


@router.get("/get-special_support-by-id/{id}")
async def get_by_id(id: int):

    special_support = special_support_service.get_special_support_with_id(id)
    if special_support is None:
        raise HTTPException(status_code=404, detail="")
    return special_support

@router.get("/get-special_support-by-name/{name}")
async def get_by_name(name: str):

    special_support = special_support_service.get_special_support_with_name(name)
    if special_support is None:
        raise HTTPException(status_code=404, detail="")
    return special_support

@router.get("/get-all-needy-speciel-supports/{id}")
async def get_by_needy_id(id: int):

    support = special_support_service.get_suppport_by_needy_id(id)
    if support is None:
        raise HTTPException(status_code=404, detail="")
    return support

@router.post("/add-special_support")
async def add_special_support(new_special_support: BaseSpecialSupportSchema=Body(...)):

    special_support =  special_support_service.create_new_special_support(new_special_support)
    if special_support is None:
        raise HTTPException(status_code=404, detail="")
    return special_support

@router.put("/update-special_support/{id}")
async def update_special_support(id: int, update: SpecialSupportSchema=Body(...)):

    special_support =  special_support_service.update_special_support(id, update)
    if special_support is None:
        raise HTTPException(status_code=404, detail="")
    return special_support

@router.delete("/delete-special_support/{id}")
async def update_special_support(id: int):

    return special_support_service.delete_allocation(id)