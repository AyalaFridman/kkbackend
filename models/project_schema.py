from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from models.allocation_schema import AllocationSchema

class BaseProjectSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True
        
class ProjectSchema(BaseProjectSchema):

    allocations: Optional[List[AllocationSchema]] = [] 

    class Config:
        orm_mode = True
        from_attributes = True

