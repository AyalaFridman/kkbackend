from models.models import ServiceProvider
from models.service_provider_schema import ServiceProviderSchema, BaseServiceProviderSchema, ServiceProviderSchemaPostNeedy
from db_config import object_manager
from typing import List


# Function to get all records
def get_all_service_providers() -> List[BaseServiceProviderSchema]:

    service_providers = object_manager.get_objects(
        base_table=ServiceProvider,
        schema_class=BaseServiceProviderSchema,
        relationships=[ServiceProvider.special_supports],  
        filters=None,  
    )
    return service_providers


def get_service_provider_with_id(id: int) -> ServiceProviderSchema:
    filters = [ServiceProvider.id == id] 
    result = object_manager.get_objects(
        base_table=ServiceProvider,
        schema_class=ServiceProviderSchema,
        relationships=[       
            ServiceProvider.special_supports, 
            ServiceProvider.cashbox,  
            ServiceProvider.payments   
        ],
        filters=filters
    )
    return result

def get_service_provider_with_name(name: str) -> ServiceProviderSchema:
    
    filters = [ServiceProvider.name == name] 
    result = object_manager.get_objects(
        base_table=ServiceProvider, schema_class=ServiceProviderSchema, filters=filters
    )
    return result[0]

def create_new_service_provider(service_provider_data:ServiceProviderSchemaPostNeedy)-> ServiceProviderSchema:

    service_provider_dict = service_provider_data.dict()
    new_service_provider = ServiceProvider(**service_provider_dict)
    return object_manager.add_object(new_service_provider)

def update_service_provider(id: int, update: ServiceProviderSchema)-> ServiceProviderSchema:
    
    filters = [ServiceProvider.id == id]
    update = update.dict(exclude_unset=True)
    service_providers =  object_manager.update_objects(ServiceProvider,ServiceProviderSchema, filters=filters, updates=update)
    print(service_providers)
    return service_providers

def delete_service_provider(id: int):
    
    filters = [ServiceProvider.id == id]
    return object_manager.delete_objects(ServiceProvider, filters)
    

