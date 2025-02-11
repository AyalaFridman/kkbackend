# from models.model import Fund
from DAL import fund_repo
from typing import List
from models.fund_schema import FundSchema

def get_all_funds() -> List[FundSchema]:
    
    result = fund_repo.get_all_funds()
    return result

def get_all_direct_family_funds() -> List[FundSchema]:
    
    result = fund_repo.get_all_direct_family_funds()
    return result

def get_fund_with_id(id:int) -> FundSchema:
    result = fund_repo.get_fund_with_id(id)
    return result

def get_fund_with_name(name:str) -> FundSchema:
    result = fund_repo.get_fund_with_name(name)
    return result

def get_fund_allocation(id:int):
    result = fund_repo.get_fund_with_id(id)
    print(result)
    return result[0].allocations

def create_new_fund(new_project:FundSchema )-> FundSchema:

    return fund_repo.create_new_fund(new_project)

def update_fund(id: int, update: FundSchema)-> FundSchema:

    return fund_repo.update_fund(id, update)

def delete_fund(id: int):
    
    return fund_repo.delete_fund(id)