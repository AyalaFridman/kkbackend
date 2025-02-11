# services/addresses_service.py
from  models.models import Address
from DAL import addresses_repo
from typing import List


# פונקציה לקבלת כל הנתונים
def get_all_addresses() -> List[Address]:
    result = addresses_repo.get_all_addresses()
    return result
def get_address_by_id(id:int) -> Address:
    result = addresses_repo.get_address_by_id(id)
    return result
def create_address(new_address:Address) -> Address:
    result = addresses_repo.create_address(new_address)
    return result