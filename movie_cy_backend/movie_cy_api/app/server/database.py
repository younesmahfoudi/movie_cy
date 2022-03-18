import motor.motor_asyncio
from bson.objectid import ObjectId


##MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb://root:pass12345@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.movies

group_collection = database.get_collection("Group")

def group_helper(group) -> dict:
    return {
        "nom": group["nom"],
        "membres": group["membres"],
        "admin": group["admin"],
        "photo": group["photo"],
    }

# Retrieve a group with a matching ID
async def retrieve_group(id: str) -> dict:
    group = await group_collection.find_one({"_id": ObjectId(id)})
    if group:
        return group_helper(group)

# Retrieve all groups present in the database
async def retrieve_groups():
    groups = []
    async for group in group_collection.find():
        groups.append(group_helper(group))
    return groups


# Add a new group into to the database
async def add_group(group_data: dict) -> dict:
    group = await group_collection.insert_one(group_data)
    new_group = await group_collection.find_one({"_id": group.inserted_id})
    return group_helper(new_group)


# Update a group with a matching ID
async def update_group(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    group = await group_collection.find_one({"_id": ObjectId(id)})
    if group:
        updated_group = await group_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_group:
            return True
        return False


# Delete a group from the database
async def delete_group(id: str):
    group = await group_collection.find_one({"_id": ObjectId(id)})
    if group:
        await group_collection.delete_one({"_id": ObjectId(id)})
        return True 


user_collection = database.get_collection("User")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "nom": user["nom"],
        "prenom": user["prenom"],
        "email": user["email"],
        "mdp": user["mdp"],
        "films": user["films"],
        "groupes": user["groupes"],
        "mood": user["mood"],
        "acteur": user["acteur"],
        "realisateur": user["realisateur"],
        "genre": user["genre"],
        "genreFlex": user["genreFlex"],
        "ddn": user["ddn"],
        "age": user["age"],
    }

# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Retrieve all users present in the database
async def retrieve_users():
    users = []
    print("Get Users")
    print(user_collection.find())
    async for user in user_collection.find():
        print(users)
        users.append(user_helper(user))
    return users

