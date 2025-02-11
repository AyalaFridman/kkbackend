from fastapi import APIRouter, Body, HTTPException, Depends
from services import child_service
from models.child_schema import ChildrenSchema
router = APIRouter()


@router.post("/post-child", status_code=201)
def post_needy(new_child: ChildrenSchema):
    '''Create a new child'''
    result = child_service.create_child(new_child)
    if result is None:
        raise HTTPException(status_code=400, detail="Error creating child")
    return result