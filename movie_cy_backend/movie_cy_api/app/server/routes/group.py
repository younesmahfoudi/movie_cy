from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_group,
    delete_group,
    retrieve_group,
    retrieve_groups,
    update_group,
    add_user_to_a_group
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
    print(new_group)
    if 'nom' in new_group.keys():
        return ResponseModel(new_group, "group added successfully.")     
    else :
        raise HTTPException(status_code=404, detail=new_group["message"])

@router.get("/", response_description="Groups retrieved")
async def get_groups():
    groups = await retrieve_groups()
    if groups:
        return ResponseModel(groups, "Groups data retrieved successfully")
    return ResponseModel(groups, "Empty list returned")


@router.get("/{id}", response_description="Group data retrieved")
async def get_group_data(id):
    group = await retrieve_group(id)
    if group:
        return ResponseModel(group, "Group data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Group doesn't exist.")

@router.put("/{id}")
async def update_group_data(id: str, req: UpdateGroupModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_group = await update_group(id, req)
    if updated_group:
        return ResponseModel(
            "Group with ID: {} name update is successful".format(id),
            "Group name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the group data.",
    )


@router.put("/{id}/users/{idUser}")
async def update_group_members_data(id: str, idUser:str):
    updated_group = await add_user_to_a_group(id,idUser)
    if updated_group:
        return ResponseModel(
            "Group with ID: {} name update is successful".format(id),
            "Group name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the group data.",
    )



@router.delete("/{id}", response_description="Group data deleted from the database")
async def delete_group_data(id: str):
    deleted_group = await delete_group(id)
    if deleted_group:
        return ResponseModel(
            "Group with ID: {} removed".format(id), "Group deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Group with id {0} doesn't exist".format(id)
    )   