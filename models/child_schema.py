from datetime import date
from typing import Optional
from pydantic import BaseModel


class ChildrenSchema(BaseModel):
    needy_id:int
    name: str
    child_id:str
    birth_date:date
    place_of_study:str
    tuition_amount:int
    additional_expenses:Optional[int] = None
    class Config:
        orm_mode = True
        from_attributes = True