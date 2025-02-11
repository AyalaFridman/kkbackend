from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from models.base_support_schema import BaseSupportSchema, BaseSupportSchemaPost
from models.service_provider_schema import ServiceProviderSchema, BaseServiceProviderSchema

class BaseSpecialSupportSchema(BaseSupportSchemaPost):
    service_provider_id: int
    # service_provider: Optional[ServiceProviderSchema] = None
    
class SpecialSupportSchema(BaseSupportSchema):
    # service_provider_id: int
    service_provider: Optional[BaseServiceProviderSchema] = None