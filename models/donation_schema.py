from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class DonationSchema(BaseModel):
    amount: float = None  
    currency: Optional[str] = None 
    transaction_time: str = Field(default=None, alias="transactionTime") 
    last_num: Optional[str] = Field(default=None, alias="lastNum") 
    transaction_type: Optional[str] = Field(default=None, alias="transactionType")
    groupe: Optional[str] = None 
    tashloumim: Optional[int] = None 
    first_tashloum: Optional[float] = Field(default=None, alias="firstTashloum")
    next_tashloum: Optional[float] = Field(default=None, alias="nextTashloum") 
    source:Optional[str] = None
    class Config:
        orm_mode = True
        from_attributes = True
        population_by_field_name = True
        




