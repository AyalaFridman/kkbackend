from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from models.project_schema import ProjectSchema
from models.address_schema import AddressSchema
from models.base_support_schema import BaseSupportSchema
from models.cashBox_schema import CashBoxSchema
from models.payments_schema import PaymentsSchemaGet
class BaseServiceProviderSchema(BaseModel):
    id: int
    name: Optional[str] = None
    phone: Optional[str]=None
    email: str
    city: Optional[str] = None
    street: Optional[str] = None
    building_number: Optional[int]=None
    apartment_number: Optional[int] = None
    type_of_service: str
    account_owner_name: str
    account_number: str
    bank_number: str
    branch_number: str
    provider_type: str  # "needy" או "cashbox"


    class Config:
        orm_mode = True  # מאפשר פיצ'ר ORM של SQLAlchemy לעבוד בצורה תקינה
        from_attributes = True

class ServiceProviderSchema(BaseServiceProviderSchema):
    
    address: Optional[AddressSchema] = None 
    special_supports: Optional[List[BaseSupportSchema]] = None  # אם יש קשר עם SpecialSupport
    cashbox: Optional[List[CashBoxSchema]] = None  # אם יש קשר עם CashBox
    payments: Optional[List[PaymentsSchemaGet]] = None

    class Config:
        orm_mode = True  
        from_attributes = True 
            
class ServiceProviderSchemaPostNeedy(BaseServiceProviderSchema):
    address_id: Optional[int] = None 
    # special_supports_id: Optional[int] = None
    # cashbox_id: Optional[int] = None

    class Config:
        orm_mode = True 
        from_attributes = True