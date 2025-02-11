
from pydantic import BaseModel
from typing import  Optional

class AddressSchema(BaseModel):
    city: str
    street: str
    building_number: Optional[int]=None
    class Config:
        orm_mode = True
        from_attributes = True
