from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

from app.server.database import (
    add_user, delete_group, retrieve_group, retrieve_user, retrieve_users, retrieve_users_filtered, update_group,update_user,delete_user,
)
from app.server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
    UserLoginSchema
)

router = APIRouter()

async def check_user(data: UserLoginSchema):
    for user in await get_users():
        if user["email"] == data.email and user["mdp"] == data.mdp:
            return user


@router.post("/signup", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    if new_user:
        return signJWT(new_user["id"])
    return ErrorResponseModel("An error occurred.", 404, "User already exist.")


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    userData = await check_user(user)
    if userData:
        return signJWT(userData["id"])
    return {
        "error": "Wrong login details!"
    }

@router.get("/", response_description="Users retrieved")
async def get_users(string_entered: str | None= None):
    if(type(string_entered)==str):
        users = await retrieve_users_filtered(string_entered)
    else :
      users = await retrieve_users() 
    if users:
        return users
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")


@router.put("/{id}", dependencies=[Depends(JWTBearer())])
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", dependencies=[Depends(JWTBearer())],response_description="User data deleted from the database")
async def delete_user_data(id: str):
    user = await get_user_data(id)
    if user: 
        for group in user["data"][0]["groupes"]: 
            item = await retrieve_group(group)
            if item:
                # Cas où l'utilisateur supprimé est admin du groupe
                if(item["admin"]==id):
                    # Cas où il y a d'autres membres dans le groupe
                    if(len(item["membres"])>1):
                      # On donne le rôle d'admin à un autre membre
                      item["membres"] = list(filter(lambda user: user!=id, item["membres"]))
                      item["admin"] = item["membres"][0]
                      await update_group(item["id"], item)
                    # Cas où l'utilisateur supprimé est admin et tout seul dans le groupe
                    else: 
                        await delete_group(item["id"])
                else :
                    item["membres"] = list(filter(lambda user: user!=id, item["membres"]))
                    await update_group(item["id"], item)
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
    )   