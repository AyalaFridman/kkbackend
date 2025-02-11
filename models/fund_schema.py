from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from models.allocation_schema import AllocationSchema


class BaseFundSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    contact_name:Optional[str] = None
    phone:Optional[str] = None
    mail:Optional[str] = None
    type: str

    class Config:
        orm_mode = True
        from_attributes = True
        
class FundSchema(BaseFundSchema):
    allocations: Optional[List[AllocationSchema]] = [] 

    class Config:
        orm_mode = True
        from_attributes = True
class FundPostSchema(BaseModel):
    name: str
    description: Optional[str] = None
    contact_name:Optional[str] = None
    phone:Optional[str] = None
    mail:Optional[str] = None
    class Config:
        orm_mode = True
        from_attributes = True