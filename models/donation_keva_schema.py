from datetime import date
from pydantic import BaseModel

class DonationsKevaSchema(BaseModel):
    # id: int
    donors_id: int
    status: bool
    monthly_amount: float | None
    currency: str | None
    category: str | None
    notes: str | None
    balance_of_charges: int | None
    were_carried_out: int | None
    next_charge: str | None
    error: str | None
    validity: str | None
    last_4_digits: str | None
    creationDate: str

    class Config:
        from_attributes = True
        

        

