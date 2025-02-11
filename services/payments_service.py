# from models.model import Fund
from DAL import payments_repo
from typing import List
from models.payments_schema import BasePaymentsSchema, PaymentsSchemaGet

# פונקציה לקבלת כל הנתונים
def get_all_payments() -> List[PaymentsSchemaGet]:
    
    return payments_repo.get_all_payments()

def get_payment_with_id(id:int) -> PaymentsSchemaGet:
    return payments_repo.get_payment_with_id(id)



def add_payment(new_payment:BasePaymentsSchema )-> BasePaymentsSchema:

    return payments_repo.add_payment(new_payment)


