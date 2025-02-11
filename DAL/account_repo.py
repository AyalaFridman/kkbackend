
from models.schema import AccountSchema
from db_config import object_manager
from models.models import Account

def update_account(id: int, update:AccountSchema ) -> AccountSchema:
    filters = [Account.id == id]
    update = update.dict(exclude_unset=True)
    account = object_manager.update_objects(Account, AccountSchema, filters=filters, updates=update)
    print(account)
    return account
