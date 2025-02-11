from typing import List

from models.expense_schema import ExpenseSchema, ExpenseSchemaPost
from DAL import expense_repo
def update_expense(updates: ExpenseSchema)-> ExpenseSchema:

    return expense_repo.update_expense(updates)


def create_new_expense(new_expense:ExpenseSchemaPost )-> ExpenseSchemaPost:

    return expense_repo.add_expense(new_expense)

def delete_expense(expense_id: int):
    
    return expense_repo.delete_expense(expense_id)