from pydantic import BaseModel
from typing import Optional, List
# from models.project_schema import BaseProjectSchema
# from models.fund_schema import BaseFundSchema

class AllocationSchema(BaseModel):
    id: int
    project_id: int
    fund_id: int
    allocation_type: Optional[str] = None
    allocation_method: Optional[str] = None
    amount_or_quantity: Optional[float] = None
    distributed: Optional[float] = None


    class Config:
        orm_mode = True
        from_attributes = True
