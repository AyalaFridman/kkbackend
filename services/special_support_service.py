# from models.model import special_support
from DAL import special_support_repo
from typing import List
from models.special_support_schema import SpecialSupportSchema, BaseSpecialSupportSchema

def get_all_special_supports() -> List[SpecialSupportSchema]:
    
    result = special_support_repo.get_all_special_supports()
    return result

def get_special_support_with_id(id:int) -> SpecialSupportSchema:
    result = special_support_repo.get_special_support_with_id(id)
    return result

def get_special_support_with_name(name:str) -> SpecialSupportSchema:
    result = special_support_repo.get_special_support_with_name(name)
    return result

def get_suppport_by_needy_id(id:int) -> List[SpecialSupportSchema]:
    result = special_support_repo.get_suppport_by_needy_id(id)
    return result

def create_new_special_support(new_project:BaseSpecialSupportSchema )-> SpecialSupportSchema:

    return special_support_repo.create_new_special_support(new_project)

def update_special_support(id: int, update: SpecialSupportSchema)-> SpecialSupportSchema:

    return special_support_repo.update_special_support(id, update)

def delete_special_support(id: int):
    
    return special_support_repo.delete_special_support(id)