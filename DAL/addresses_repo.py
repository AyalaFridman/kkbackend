from models.models import Address
from db_config import object_manager
from typing import List

def get_all_addresses() -> List[Address]:
    result = object_manager.get_objects(Address)
    return result


def get_address_by_id(id: int) -> Address:
    result = object_manager.get_objects(Address, filters={"id": id})
    return result
def create_address(new_address:Address) -> Address:
    result = object_manager.add_object(new_address)
    return result
