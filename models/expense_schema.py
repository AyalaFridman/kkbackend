from pydantic import BaseModel
from typing import List, Optional

class BaseExpenseSchema(BaseModel):
    expense_type: str | None = None
    description: str | None = None
    amount: float | None = None

    class Config:
        orm_mode = True
        from_attributes = True
        
class ExpenseSchema(BaseExpenseSchema):
    id: int = 0

    class Config:
        orm_mode = True
        from_attributes = True
        
class ExpenseSchemaPost(BaseExpenseSchema):
    needy_id: int 
    
    class Config:
        orm_mode = True
        from_attributes = True