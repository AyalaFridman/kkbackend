from typing import List

from models.Income_schema import IncomeSchema, IncomeSchemaPost
from DAL import income_repo
def update_income(updates: IncomeSchema)-> List[IncomeSchema]:

    return income_repo.update_income(updates)


def create_new_income(new_income:IncomeSchemaPost )-> IncomeSchemaPost:

    return income_repo.add_income(new_income)

def delete_income(income_id: int):
    
    return income_repo.delete_income(income_id)