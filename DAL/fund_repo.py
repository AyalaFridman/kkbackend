import pdb

from models.models import Fund
from models.fund_schema import FundPostSchema, FundSchema
from db_config import object_manager
from typing import List


# Function to get all records
def get_all_funds() -> List[FundSchema]:

    funds = object_manager.get_objects(
        base_table=Fund,
        schema_class=FundSchema,
        relationships=[Fund.allocations],
        filters=[Fund.type == "עזרה לקופה"], 
    )
    return funds

def get_all_direct_family_funds() -> List[FundSchema]:
    funds = object_manager.get_objects(base_table=Fund,
        schema_class=FundSchema,
        relationships=[Fund.allocations],
        filters=[Fund.type == "עזרה למשפחות"], )
    return funds
    
def get_fund_with_id(id: int) -> FundSchema:

    filters = [Fund.id == id]  # תנאי ספציפי
    result = object_manager.get_objects(
        base_table=Fund, schema_class=FundSchema, relationships=[Fund.allocations], filters=filters
    )
    return result

def get_fund_with_name(name: str) -> FundSchema:
    
    filters = [Fund.name == name] 
    result = object_manager.get_objects(
        base_table=Fund, schema_class=FundSchema, relationships=[Fund.allocations], filters=filters
    )
    return result[0]

def create_new_fund(fund_data:FundPostSchema)-> FundSchema:

    fund_dict = fund_data.dict()

    new_fund = Fund(**fund_dict)
    return object_manager.add_object(new_fund)

def update_fund(id: int, update: FundSchema)-> FundSchema:
    
    filters = [Fund.id == id]
    update = update.dict(exclude_unset=True)
    funds =  object_manager.update_objects(Fund,FundSchema, filters=filters, updates=update)
    print(funds)
    return funds

def delete_fund(id: int):
    
    filters = [Fund.id == id]
    return object_manager.delete_objects(Fund, filters)
    

