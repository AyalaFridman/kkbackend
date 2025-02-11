from fastapi import APIRouter, Body, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from models.models import Needy
from services import needy_service
from models.schema import NeedySchema
from models.needy_put_schema import NeedyPutSchema


router = APIRouter()

@router.get("/get-all-needy")
def get_all():
    '''Get all needy'''
    print("in cont")
    needy = needy_service.get_all_needy()
    return needy


@router.get("/get-needy-by-id/{id}")
async def get_by_id(id: int):
    '''Get needy by id'''
    needy = needy_service.get_needy_with_detial(id)
    if needy is None:
        raise HTTPException(status_code=404, detail="Needy not found")
    return needy
@router.get("/get-needy-by-tz/{tz}")
async def get_by_tz(tz: str):
    needy = needy_service.get_needy_by_tz(tz)
    if needy is None:
        raise HTTPException(status_code=404, detail="Needy not found")
    return needy

@router.post("/post-needy",status_code=201)
async def post_needy(new_needy:NeedySchema= Body(...)):
    '''Create a new needy'''
    result = needy_service.create_needy(new_needy)
    if result is None:
        raise HTTPException(status_code=400, detail="Error creating needy")
    return result

@router.put("/put-needy/{id}", response_model=NeedyPutSchema)
def put_needy(id: int, update_needy:NeedyPutSchema= Body(...)):
    '''Update needy by id'''
    print("in update")
    result =needy_service.update_needy(id, update_needy)
    if result is None:
        raise HTTPException(status_code=404, detail="Needy not found or update failed")
    return result
@router.put("/put-needy-status/{id}")
def put_needy_status(id: int, status:bool):
    result =needy_service.update_needy_status(id, status)
    if result is None:
        raise HTTPException(status_code=404, detail="Needy not found or update failed")
    return result

@router.delete("/delete-needy/{id}", status_code=204)
async def delete_needy(id: int):
    '''Delete needy by id'''
    result=needy_service.delete_needy(id)
    if not result:
        raise HTTPException(status_code=404, detail="Needy not found")
    return {"message": "Needy deleted successfully"}

