from typing import List, Optional
from pydantic import BaseModel

class Payment(BaseModel):

    payment_type: int=None
    payment_sum: int = None
    # checks_number: Optional[int] = None
    bt_bank_branch: Optional[int] = None
    bt_bank_account:Optional[int] = None
    comment:Optional[str] = None
    class Config:
        orm_mode = True
        from_attributes = True
     

class RecepitSchema(BaseModel):
    description: Optional[str] = None
    customer_zeout:str = None
    customer_name: str = None
    customer_email: Optional[str] = None
    customer_address:Optional[str] = None
    payment: List[Optional[Payment]] = None
    price_total: int=None
    comment: Optional[str] = None
    send_copy: Optional[int] = None
    email_text:Optional[str] = None
    class Config:
        orm_mode = True
        from_attributes = True
    
           

