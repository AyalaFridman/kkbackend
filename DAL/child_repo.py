
from models.child_schema import ChildrenSchema
from models.models import Child
from db_config import object_manager

def create_child(new_child:ChildrenSchema):
    child_instance = Child(**new_child.dict())
    result = object_manager.add_object(child_instance)
    return child_instance