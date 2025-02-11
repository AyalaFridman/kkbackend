from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from services import project_service
from models.project_schema import ProjectSchema

router = APIRouter()

@router.get("/get-all-projects")
def get_all():
    
    results = project_service.get_all_projects()
    return results


@router.get("/get-project-by-id/{id}")
async def get_by_id(id: int):

    project = project_service.get_project_with_id(id)
    if project is None:
        raise HTTPException(status_code=404, detail="")
    return project

@router.get("/get-project-allocation/{id}")
async def get_project_allocation(id: int):

    project = project_service.get_project_allocation(id)
    if project is None:
        raise HTTPException(status_code=404, detail="")
    return project

@router.get("/get-project-by-name/{name}")
async def get_by_name(name: str):

    project = project_service.get_project_with_name(name)
    if project is None:
        raise HTTPException(status_code=404, detail="")
    return project


@router.post("/add-project")
async def add_project(new_project: ProjectSchema=Body(...)):

    project =  project_service.create_new_project(new_project)
    if project is None:
        raise HTTPException(status_code=404, detail="")
    return project

@router.put("/update-project/{id}")
async def update_project(id: int, update: ProjectSchema=Body(...)):

    project =  project_service.update_project(id, update)
    if project is None:
        raise HTTPException(status_code=404, detail="")
    return project

@router.delete("/delete-project/{id}")
async def update_project(id: int):

    return project_service.delete_project(id)


