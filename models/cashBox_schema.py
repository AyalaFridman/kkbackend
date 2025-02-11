from pydantic import BaseModel
from typing import List
# from models.service_provider_schema import ServiceProviderSchema  # ייבוא של ServiceProvider

class CashBoxSchema(BaseModel):
    id: int
    name: str
    balance: int = 0  # ברירת מחדל לאפס

    # קשרים עם טבלאות אחרות:
    # service_providers: List[ServiceProviderSchema] = []  # קשר עם ServiceProvider

    class Config:
        orm_mode = True
        from_attributes = True
