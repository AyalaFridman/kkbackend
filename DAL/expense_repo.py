from typing import List

from models.expense_schema import ExpenseSchema, ExpenseSchemaPost
from db_config import object_manager
from models.models import Expense

def update_expense(updates:ExpenseSchema ) ->ExpenseSchema:
    
    filters = [Expense.id == updates.id]
    update = updates.dict(exclude_unset=True)
    expense = object_manager.update_objects(Expense, ExpenseSchema, filters=filters, updates=update)
    return expense

def add_expense(expense_data: ExpenseSchemaPost) -> ExpenseSchemaPost:
    expense_dict = expense_data.dict()
    new_expense = Expense(**expense_dict)
    return object_manager.add_object(new_expense)

def delete_expense(expense_id: int):
    filters = [Expense.id == expense_id]
    return object_manager.delete_objects(Expense, filters)
