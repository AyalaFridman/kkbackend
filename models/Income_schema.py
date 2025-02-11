from pydantic import BaseModel
from typing import List, Optional

class BaseIncomeSchema(BaseModel):
    income_type: str | None = None
    description: str | None = None
    amount: float | None = None

    class Config:
        orm_mode = True
        from_attributes = True
        
class IncomeSchema(BaseIncomeSchema):
    id: int = 0


    class Config:
        orm_mode = True
        from_attributes = True
        
class IncomeSchemaPost(BaseIncomeSchema):
    needy_id: int 
    
    class Config:
        orm_mode = True
        from_attributes = True