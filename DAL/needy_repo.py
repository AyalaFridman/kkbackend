from models.models import *
from models.schema import *
from models.needy_put_schema import NeedyPutSchema
from db_config import object_manager
from typing import List, Type, TypeVar

def get_all_needy() -> List[Needy]:
    result = object_manager.get_objects_whithout_rel(model_class=Needy)
    return result

def get_needy_with_detial(id:int) -> NeedyGetSchema:
    print("in repo",id)
    filters = [
    Needy.id == id 
    ]
    result=object_manager.get_objects(base_table=Needy,schema_class=NeedyGetSchema,relationships=[Needy.children,Needy.expenses,Needy.income,Needy.account],filters=filters)
    return result 
def get_needy_by_tz(tz:str) -> Needy:
    filters = [
    (Needy.id_husband == tz) | (Needy.id_wife==tz )
    ]
    result=object_manager.get_objects(base_table=Needy,schema_class=NeedySchema,filters=filters)
    return result 
def delete_needy(id:int):
    filters = [
    Needy.id == id 
    ]
    object_manager.delete_objects(Needy,filters)

def update_needy(id:int,update):
    filters = [
        Needy.id == id
    ]
    update = update.dict(exclude_unset=True)
    result=object_manager.update_objects(Needy,NeedyPutSchema,filters=filters,updates=update)
    return result
def update_needy_status(id:int,status:bool):
    filters = [
        Needy.id == id
    ]
    result=object_manager.update_objects(Needy,NeedyPutSchema,filters=filters,updates={"status":status})
    return result

def create_needy(new_needy:NeedySchema):
    print("new_needy: ",new_needy)
    # needy_instance = Needy(**new_needy.dict())
    result=object_manager.create_needy(new_needy)
    return result
