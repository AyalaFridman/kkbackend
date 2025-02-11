from models.models import Payment
from models.payments_schema import BasePaymentsSchema, PaymentsSchemaGet
from db_config import object_manager
from typing import List

def get_all_payments() -> List[PaymentsSchemaGet]:

    return object_manager.get_objects(
        base_table=Payment,
        schema_class=PaymentsSchemaGet,
        filters=None, 
    )


def get_payment_with_id(id: int) -> PaymentsSchemaGet:

    filters = [Payment.id == id]
    result = object_manager.get_objects(
        base_table=Payment, schema_class=PaymentsSchemaGet, filters=filters
    )
    return result


def add_payment(payment_data:BasePaymentsSchema)-> BasePaymentsSchema:

    payment_dict = payment_data.dict(exclude_unset=True)
    new_payment = Payment(**payment_dict)
    
    object_manager.add_object(new_payment)
    # return get_payment_with_id(payment_data.id)

    

