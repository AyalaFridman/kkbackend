# services/needy_service.py
from models.needy_put_schema import NeedyPutSchema
from models.models import Needy
from DAL import needy_repo
from typing import List
from models.schema import NeedyGetSchema, NeedySchema
# פונקציה לקבלת כל הנתונים
def get_all_needy() -> List[Needy]:
    print("in service")
    result = needy_repo.get_all_needy()
    return result

def get_needy_with_detial(id:int) -> NeedyGetSchema:
    result = needy_repo.get_needy_with_detial(id)
    return result
def get_needy_by_tz(tz:str) -> NeedySchema:
    result = needy_repo.get_needy_by_tz(tz)
    return result

def delete_needy(id:int):
    needy_repo.delete_needy(id)

def update_needy(id:int,update:Needy):
    result=needy_repo.update_needy(id,update)
    return result
def update_needy_status(id:int,status:bool):
    result=needy_repo.update_needy_status(id,status)
    return result
def create_needy(new_needy:NeedySchema):
    result=needy_repo.create_needy(new_needy)
    return result