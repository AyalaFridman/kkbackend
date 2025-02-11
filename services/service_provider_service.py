# from models.model import service_provider
from DAL import service_provider_repo
from typing import List
from models.service_provider_schema import ServiceProviderSchema, BaseServiceProviderSchema, ServiceProviderSchemaPostNeedy

def get_all_service_providers() -> List[BaseServiceProviderSchema]:
    
    result = service_provider_repo.get_all_service_providers()
    return result

def get_service_provider_with_id(id:int) -> ServiceProviderSchema:
    result = service_provider_repo.get_service_provider_with_id(id)
    return result

def get_service_provider_with_name(name:str) -> ServiceProviderSchema:
    result = service_provider_repo.get_service_provider_with_name(name)
    return result

def create_new_service_provider(new_project:ServiceProviderSchemaPostNeedy )-> ServiceProviderSchema:

    return service_provider_repo.create_new_service_provider(new_project)

def update_service_provider(id: int, update: ServiceProviderSchema)-> ServiceProviderSchema:

    return service_provider_repo.update_service_provider(id, update)

def delete_service_provider(id: int):
    
    return service_provider_repo.delete_service_provider(id)