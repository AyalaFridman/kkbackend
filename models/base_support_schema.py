
from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.schema import BaseNeedy

class BaseSupportSchemaPost(BaseModel):
    needy_id: int
    amount: float
    date: str
    notes: Optional[str] = None
    
    class Config:
        orm_mode = True
        from_attributes = True
class BaseSupportSchema(BaseSupportSchemaPost):
    id:int
    needy : BaseNeedy

    class Config:
        orm_mode = True
        from_attributes = True