from typing import List

from models.Income_schema import IncomeSchema, IncomeSchemaPost
from models.models import Income
from db_config import object_manager

def update_income(update:List[IncomeSchema ]) -> List[IncomeSchema]:

    filters = [Income.id == update.id]
    update = update.dict(exclude_unset=True)
    return object_manager.update_objects(Income, IncomeSchema, filters=filters, updates=update)


def add_income(income_data: IncomeSchemaPost) -> IncomeSchemaPost:
    income_dict = income_data.dict()
    new_income = Income(**income_dict)
    return object_manager.add_object(new_income)

def delete_income(income_id: int):
    filters = [Income.id == income_id]
    return object_manager.delete_objects(Income, filters)
