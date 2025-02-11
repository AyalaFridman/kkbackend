from models.models import SpecialSupport
from models.special_support_schema import SpecialSupportSchema, BaseSpecialSupportSchema
from db_config import object_manager
from typing import List

def get_all_special_supports() -> List[SpecialSupportSchema]:

    special_supports = object_manager.get_objects(
        base_table=SpecialSupport,
        schema_class=SpecialSupportSchema,
    )
    return special_supports


def get_special_support_with_id(id: int) -> SpecialSupportSchema:

    filters = [SpecialSupport.id == id] 
    result = object_manager.get_objects(
        base_table=SpecialSupport, schema_class=SpecialSupportSchema, filters=filters
    )
    return result[0]

def get_special_support_with_name(name: str) -> SpecialSupportSchema:
    
    filters = [SpecialSupport.name == name]
    result = object_manager.get_objects(
        base_table=SpecialSupport, schema_class=SpecialSupportSchema, filters=filters
    )
    return result[0]

def get_suppport_by_needy_id(id:int) -> List[SpecialSupportSchema]:

    supports = object_manager.get_objects(
        base_table=SpecialSupport,
        schema_class=SpecialSupportSchema,
        filters=[SpecialSupport.needy_id== id], 
    )
    return supports

def create_new_special_support(special_support_data:BaseSpecialSupportSchema)-> SpecialSupportSchema:

    special_support_dict = special_support_data.dict()
    new_special_support = SpecialSupport(**special_support_dict)
    return object_manager.add_object(new_special_support)

def update_special_support(id: int, update: SpecialSupportSchema)-> SpecialSupportSchema:
    
    filters = [SpecialSupport.id == id]
    update = update.dict(exclude_unset=True)
    special_supports =  object_manager.update_objects(SpecialSupport,SpecialSupportSchema, filters=filters, updates=update)
    print(special_supports)
    return special_supports

def delete_special_support(id: int):
    
    filters = [SpecialSupport.id == id]
    return object_manager.delete_objects(SpecialSupport, filters)
    

