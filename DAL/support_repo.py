from DAL import allocation_repo
from models.models import Support, Needy
from models.support_schema import SupportSchema, BaseSupport
from db_config import object_manager
from typing import List

def get_all_supports() -> List[SupportSchema]:

    supports = object_manager.get_objects(
        base_table=Support,
        schema_class=SupportSchema,
    )
    return supports

def get_suppport_by_needy_id(id:int) -> List[SupportSchema]:

    supports = object_manager.get_objects(
        base_table=Support,
        schema_class=SupportSchema,
        filters=[Support.needy_id== id], 
    )
    return supports

def get_support_with_allocation_id(id: int) -> List[SupportSchema]:
    
    filters = [Support.allocations_id == id]
    result = object_manager.get_objects(
        base_table=Support, schema_class=SupportSchema, filters=filters
    )
    return result

def get_support_with_id(id: int) -> SupportSchema:

    filters = [Support.id == id] 
    result = object_manager.get_objects(
        base_table=Support, schema_class=SupportSchema, filters=filters
    )
    
    return result[0]

def get_support_with_name(name: str) -> SupportSchema:
    
    filters = [Support.name == name]
    result = object_manager.get_objects(
        base_table=Support, schema_class=SupportSchema, filters=filters
    )
    return result[0]


def create_new_support(support_data:BaseSupport)-> BaseSupport:
    print("hellooooo")
    support_dict = support_data.dict(exclude_unset=True)
    new_support = Support(**support_dict)
    print("support",new_support.allocations_id)
    result=allocation_repo.update_amount_of_allocation(new_support.allocations_id,new_support.amount)
    print(result)
    if result!="Not enough amount in allocation":
        return object_manager.add_object(new_support)
    else:
        print("oo")
        return result

def update_support(id: int, update: BaseSupport)-> BaseSupport:
    
    filters = [Support.id == id]
    update = update.dict(exclude_unset=True)
    supports =  object_manager.update_objects(Support,BaseSupport, filters=filters, updates=update)
    print(supports)
    return supports

def delete_support(id: int):
    
    filters = [Support.id == id]
    return object_manager.delete_objects(Support, filters)
    

