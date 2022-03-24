import datetime
from enum import unique
from typing import List, Optional
from app.server.models.movie import Genre, StarList
import motor.motor_asyncio
from bson.objectid import ObjectId


##MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb://root:pass12345@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.MOVIECYDB

group_collection = database.get_collection("GROUPS")

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


user_collection = database.get_collection("USERS")

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
        "avatar": user["avatar"]
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


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True 

movie_collection = database.get_collection("MOVIES")

# database.get_collection("MOVIES").create_index("id", unique= True)

def movie_helper(movie) -> dict:
    return {
        "id": movie["id"],
        "image": movie["image"],
        "title": movie["title"],
        "description": movie["description"],
        "runtimeStr": movie["runtimeStr"],
        "genres": movie["genres"],
        "genreList": movie["genreList"],
        "contentRating": "PG-13",
        "imDbRating": movie["imDbRating"],
        "imDbRatingVotes": movie["imDbRatingVotes"],
        "metacriticRating": movie["metacriticRating"],
        "plot": movie["plot"],
        "stars": movie["stars"],
        "starList": movie["starList"],
    }


# Retrieve a group with a matching ID
async def retrieve_movie_by_id(id: str) -> dict:
    movie = await movie_collection.find_one({"id": id})
    if movie:
        return movie_helper(movie)

# Retrieve a group with a matching ID
async def retrieve_movies_by_title(title: str) -> dict:
    movies = []
    async for movie in movie_collection.find({"title": title}):
        print(movie)
        movies.append(movie_helper(movie))
    return movies

# Retrieve a group with a matching ID
async def retrieve_movies_by_genre(genre: str) -> dict:
    movies = []
    async for movie in movie_collection.find({"genreList": {"$elemMatch": { "value": genre }}}):
        print(movie)
        movies.append(movie_helper(movie))
    return movies

# Retrieve a group with a matching ID
async def retrieve_movies_by_star(starId: str) -> dict:
    movies = []
    async for movie in movie_collection.find(
        { "starList": { "$elemMatch": { "id": starId } } }):
        print(movie)
        movies.append(movie_helper(movie))
    return movies

# Retrieve a group with a matching ID
async def retrieve_movies_by_stars(starList: List[str]) -> dict:
    movies = []
    for star in starList:
        async for movie in movie_collection.find(
            { "starList": { "$elemMatch": { "id": star["id"] } } }):
            print(movie)
            movies.append(movie_helper(movie))
    return movies

# Retrieve a group with a matching ID
async def retrieve_movies_by_genres(genreList: List[str]) -> dict:
    movies = []
    for genre in genreList:
        async for movie in movie_collection.find({"genreList": {"$elemMatch": { "value": genre }}}):
            movies.append(movie_helper(movie))
    return movies

# Retrieve a group with a matching ID
async def retrieve_movies_by_imdbRating(imdbRating: str) -> dict:
    movies = []
    movies = await movie_collection.find({"imdbRating": { "$gt": imdbRating }})
    if movies:
        return movies

# Retrieve all groups present in the database
async def retrieve_movies() -> dict:
    movies = []
    async for movie in movie_collection.find():
        print(movie)
        movies.append(movie_helper(movie))
    return movies


# Add a new movie into to the database
async def add_movie(movie_data: dict) -> dict:
    print(movie_data)
    movie = await movie_collection.update_one(
            {
                'id' : movie_data['id']
            }, 
            { 
                '$setOnInsert': movie_data 
            },
            upsert = True
        )
    new_movie = await movie_collection.find_one({"id": movie_data['id']})
    return movie_helper(new_movie)
    