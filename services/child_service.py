
from DAL import child_repo,needy_repo
from models.child_schema import ChildrenSchema

def create_child(new_child: ChildrenSchema) -> ChildrenSchema:
    result = child_repo.create_child(new_child)

    return result
