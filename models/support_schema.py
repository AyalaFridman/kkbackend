from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from models.base_support_schema import BaseSupportSchema, BaseSupportSchemaPost

class BaseSupport(BaseSupportSchemaPost):
    allocations_id: int
    
class SupportSchema(BaseSupportSchema):
    allocations_id: int
    