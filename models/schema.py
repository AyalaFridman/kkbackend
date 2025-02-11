from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from models.child_schema import ChildrenSchema
from models.address_schema import AddressSchema
class IncomeSchema(BaseModel):
    id: int=0
    income_type: str | None = None
    description: str | None = None
    amount: float | None = None

    class Config:
        orm_mode = True
        from_attributes = True

class ExpenseSchema(BaseModel):
    id: int = 0
    expense_type: str | None = None
    description: str | None = None
    amount: float | None = None

    class Config:
        orm_mode = True
        from_attributes = True
        
class AccountSchema(BaseModel):
    # id: int = 0
    account_owner_name: str|None
    account_number: str|None
    bank_number: str|None
    branch_number: str|None

    class Config:
        orm_mode = True
        from_attributes = True

class BaseNeedy(BaseModel):
    last_name: str
    husband_name: Optional[str] = None
    wife_name: Optional[str] = None
    
    class Config:
        orm_mode = True
        from_attributes = True

class NeedySchema(BaseModel): 
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
    children:Optional[List[ChildrenSchema]]=[]
    expenses: Optional[List[ExpenseSchema]]=[] 
    income: Optional[List[IncomeSchema]]=[]
    account:Optional[AccountSchema]=None
    email: Optional[str] = None
    total_debt: Optional[float] = 0.0
    status:bool
    one_time_support:Optional[int] = None
    reason_for_expense:Optional[str] = None
    gerim:bool
    class Config:
        orm_mode = True
        from_attributes = True
class NeedyGetSchema(NeedySchema):
    id: int   
    class Config:
        orm_mode = True
        from_attributes = True