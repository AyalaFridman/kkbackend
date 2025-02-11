from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from models.address_schema import AddressSchema
class NeedyPutSchema(BaseModel): 
    last_name: str
    husband_name: Optional[str] = None
    id_husband: Optional[str] = None
    husband_date_of_birth: Optional[date] = None
    wife_name: Optional[str] = None
    id_wife: Optional[str] = None
    wife_date_of_birth: Optional[date] = None
    marital_status: Optional[str] = None
    num_of_children: Optional[int] = 0
    num_of_minor_children: Optional[int] = 0
    num_of_unmarried_children: Optional[int] = 0
    level_of_need: Optional[int] = None
    city: Optional[str] = None
    street: Optional[str] = None
    building_number: Optional[int]=None
    apartment_number: Optional[int] = None
    phone: Optional[str] = None
    husband_phone: Optional[str] = None
    wife_phone: Optional[str] = None
    email: Optional[str] = None
    total_debt: Optional[float] = 0.0
    status:bool
    one_time_support:Optional[int] = None
    reason_for_expense:Optional[str] = None
    gerim:bool
    class Config:
        orm_mode = True
        from_attributes = True