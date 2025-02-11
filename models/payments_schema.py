from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class BasePaymentsSchema(BaseModel):
    date: str
    amount: int
    payment_method:str
    service_provider_id:int

    class Config:
        orm_mode = True
        from_attributes = True
        
class PaymentsSchemaGet(BasePaymentsSchema):

    id : int

    class Config:
        orm_mode = True
        from_attributes = True

