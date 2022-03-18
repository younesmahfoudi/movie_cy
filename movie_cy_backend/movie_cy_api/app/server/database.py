import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://root:pass12345@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("user_collection")

def user_helper(user) -> dict:
    return {
        "prenom": user["prenom"],
        "nom": user["nom"],
        "email": user["email"],
        "mdp": user["mdp"],
    }

# Add a new student into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)