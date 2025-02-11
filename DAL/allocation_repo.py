from models.models import Allocation
from models.allocation_schema import AllocationSchema
from models.allocation_details_schema import AllocationSchemaDetail
from db_config import object_manager
from typing import List


def get_all_allocations() -> List[AllocationSchema]:

    allocations = object_manager.get_objects(
        base_table=Allocation,
        schema_class=AllocationSchema,
        filters=None,
    )
    return allocations


def get_allocation_with_id(id: int) -> AllocationSchemaDetail:

    filters = [Allocation.id == id]
    result = object_manager.get_objects(
        base_table=Allocation, schema_class=AllocationSchemaDetail, filters=filters
    )
    return result[0]


def get_allocation_with_name(name: str) -> AllocationSchema:

    filters = [Allocation.name == name]
    result = object_manager.get_objects(
        base_table=Allocation, schema_class=AllocationSchema, filters=filters
    )
    return result[0]


def create_new_allocation(allocation_data: AllocationSchema) -> AllocationSchema:

    allocation_dict = allocation_data.dict()
    new_allocation = Allocation(**allocation_dict)
    return object_manager.add_object(new_allocation)


def update_allocation(id: int, update: AllocationSchema) -> AllocationSchema:

    filters = [Allocation.id == id]
    update = update.dict(exclude_unset=True)
    allocations = object_manager.update_objects(
        Allocation, AllocationSchema, filters=filters, updates=update
    )
    print(allocations)
    return allocations


def update_amount_of_allocation(allocation_id, amount: int):
    print("in allooc")

    allocation=object_manager.get_objects(Allocation,AllocationSchema,filters=[Allocation.id==allocation_id])
    if allocation[0].amount_or_quantity-allocation[0].distributed-amount>=0:
        return object_manager.update_objects(Allocation,AllocationSchema, filters=[Allocation.id == allocation[0].id], updates={"distributed":allocation[0].distributed+amount} )
    else:
        return "Not enough amount in allocation"


def delete_allocation(id: int):

    filters = [Allocation.id == id]
    return object_manager.delete_objects(Allocation, filters)
