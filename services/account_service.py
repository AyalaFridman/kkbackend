from models.schema import AccountSchema
from DAL import account_repo
def update_account(id: int, update: AccountSchema)-> AccountSchema:

    return account_repo.update_account(id, update)