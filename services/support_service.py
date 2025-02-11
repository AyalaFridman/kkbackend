# from models.model import support
from DAL import support_repo
from typing import List
from models.support_schema import SupportSchema, BaseSupport

def get_all_supports() -> List[SupportSchema]:
    
    result = support_repo.get_all_supports()
    return result

def get_support_with_id(id:int) -> SupportSchema:
    result = support_repo.get_support_with_id(id)
    return result

def get_suppport_by_needy_id(id:int) -> List[SupportSchema]:
    result = support_repo.get_suppport_by_needy_id(id)
    return result

def get_suppport_by_allocation_id(id:int) -> List[SupportSchema]:
    result = support_repo.get_support_with_allocation_id(id)
    return result

def get_support_with_name(name:str) -> SupportSchema:
    result = support_repo.get_support_with_name(name)
    return result

def create_new_support(new_support:BaseSupport )-> BaseSupport:

    return support_repo.create_new_support(new_support)

def update_support(id: int, update: BaseSupport)-> BaseSupport:

    return support_repo.update_support(id, update)

def delete_support(id: int):
    
    return support_repo.delete_support(id)