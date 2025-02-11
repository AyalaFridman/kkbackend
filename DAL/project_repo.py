from models.models import Project
from models.project_schema import ProjectSchema, BaseProjectSchema
from db_config import object_manager
from typing import List

def get_all_projects() -> List[ProjectSchema]:

    projects = object_manager.get_objects(
        base_table=Project,
        schema_class=ProjectSchema,
        relationships=[Project.allocations],
        filters=None, 
    )
    return projects


def get_project_with_id(id: int) -> ProjectSchema:

    filters = [Project.id == id]
    result = object_manager.get_objects(
        base_table=Project, schema_class=ProjectSchema, relationships=[Project.allocations], filters=filters
    )
    return result


def get_project_with_name(name: str) -> ProjectSchema:
    
    filters = [Project.name == name]
    result = object_manager.get_objects(
        base_table=Project, schema_class=ProjectSchema, relationships=[Project.allocations], filters=filters
    )
    return result[0]

from models.models import Project

def create_new_project(project_data:ProjectSchema)-> ProjectSchema:

    project_dict = project_data.dict(exclude_unset=True)
    new_project = Project(**project_dict)
    
    object_manager.add_object(new_project)
    return get_project_with_id(project_data.id)

def update_project(id: int, update: BaseProjectSchema)-> ProjectSchema:
    print(update)
    filters = [Project.id == id]
    update = update.dict(exclude_unset=True)
    project =  object_manager.update_objects(Project, BaseProjectSchema, filters=filters, updates=update, rel = ['allocations'])
    print(project)
    return project

def delete_project(id: int):
    
    filters = [Project.id == id]
    return object_manager.delete_objects(Project, filters)
    

