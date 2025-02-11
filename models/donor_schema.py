from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from models.donation_schema import DonationSchema
from models.donation_keva_schema import DonationsKevaSchema


class DonorSchema(BaseModel):
    # id: int
    zeout: Optional[str] = None
    name: str = None
    city: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    husband_phone: Optional[str] = None
    wife_phone: Optional[str] = None
    mail: Optional[str] = None
    bank : Optional[str] = None
    brunch : Optional[str] = None
    account_num : Optional[str] = None
    source_of_details : Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class DonorSchemaGet(DonorSchema):   
    id:int 
    donations_keva:Optional[List[DonationsKevaSchema]]|None
    donations:Optional[List[DonationSchema]]|None
    class Config:
        orm_mode = True
        from_attributes = True