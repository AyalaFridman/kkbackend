from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import service_provider_service
from models.service_provider_schema import ServiceProviderSchema, ServiceProviderSchemaPostNeedy

router = APIRouter()

@router.get("/get-all-service_providers")
def get_all():
    
    results = service_provider_service.get_all_service_providers()
    return results


@router.get("/get-service_provider-by-id/{id}")
async def get_by_id(id: int):

    service_provider = service_provider_service.get_service_provider_with_id(id)
    if service_provider is None:
        raise HTTPException(status_code=404, detail="")
    return service_provider

@router.get("/get-service_provider-by-name/{name}")
async def get_by_name(name: str):

    service_provider = service_provider_service.get_service_provider_with_name(name)
    if service_provider is None:
        raise HTTPException(status_code=404, detail="")
    return service_provider

@router.post("/add-service_provider")
async def add_service_provider(new_service_provider: ServiceProviderSchemaPostNeedy=Body(...)):

    service_provider =  service_provider_service.create_new_service_provider(new_service_provider)
    if service_provider is None:
        raise HTTPException(status_code=404, detail="")
    return service_provider

@router.put("/update-service_provider/{id}")
async def update_service_provider(id: int, update: ServiceProviderSchema=Body(...)):

    service_provider =  service_provider_service.update_service_provider(id, update)
    if service_provider is None:
        raise HTTPException(status_code=404, detail="")
    return service_provider

@router.delete("/delete-service_provider/{id}")
async def update_service_provider(id: int):

    return service_provider_service.delete_service_provider(id)