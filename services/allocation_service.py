# from models.model import allocation
from DAL import allocation_repo
from typing import List
from models.allocation_schema import AllocationSchema
from models.allocation_details_schema import AllocationSchemaDetail

def get_all_allocations() -> List[AllocationSchema]:
    
    result = allocation_repo.get_all_allocations()
    return result

def get_allocation_with_id(id:int) -> AllocationSchemaDetail:
    result = allocation_repo.get_allocation_with_id(id)
    return result

def get_allocation_with_name(name:str) -> AllocationSchema:
    result = allocation_repo.get_allocation_with_name(name)
    return result

def create_new_allocation(new_allocation:AllocationSchema )-> AllocationSchema:

    return allocation_repo.create_new_allocation(new_allocation)

def update_allocation(id: int, update: AllocationSchema)-> AllocationSchema:

    return allocation_repo.update_allocation(id, update)
def update_amount_of_allocation(id:int,amount:int):
    return allocation_repo.update_amount_of_allocation(id,amount)
def delete_allocation(id: int):
    
    return allocation_repo.delete_allocation(id)