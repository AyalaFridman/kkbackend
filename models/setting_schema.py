from pydantic import BaseModel
from typing import Optional, List
from datetime import date



class SettingSchema(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = True
        from_attributes = True