# from models.model import Fund
from DAL import project_repo
from typing import List
from models.project_schema import ProjectSchema

# פונקציה לקבלת כל הנתונים
def get_all_projects() -> List[ProjectSchema]:
    
    result = project_repo.get_all_projects()
    return result

def get_project_with_id(id:int) -> ProjectSchema:
    result = project_repo.get_project_with_id(id)
    return result

def get_project_allocation(id:int):
    result = project_repo.get_project_with_id(id)
    print(result)
    return result[0].allocations

def get_project_with_name(name:str) -> ProjectSchema:
    result = project_repo.get_project_with_name(name)
    return result

def create_new_project(new_project:ProjectSchema )-> ProjectSchema:

    return project_repo.create_new_project(new_project)

def update_project(id: int, update: ProjectSchema)-> ProjectSchema:

    return project_repo.update_project(id, update)

def delete_project(id: int):
    
    return project_repo.delete_project(id)

