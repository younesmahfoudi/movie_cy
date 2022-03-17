from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_group,
    delete_group,
    retrieve_group,
    retrieve_groups,
    update_group,
)
from app.server.models.group import (
    ErrorResponseModel,
    ResponseModel,
    GroupSchema,
    UpdateGroupModel,
)

router = APIRouter()


@router.post("/", response_description="group data added into the database")
async def add_group_data(group: GroupSchema = Body(...)):
    group = jsonable_encoder(group)
    new_group = await add_group(group)
    return ResponseModel(new_group, "group added successfully.")     