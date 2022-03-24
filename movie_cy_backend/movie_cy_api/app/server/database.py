from typing import List
from app.server.models.movie import StarList
import motor.motor_asyncio
from bson.objectid import ObjectId

from app.server.models.group import (
    ErrorResponseModel
)


##MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb://root:pass12345@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.MOVIECYDB

group_collection = database.get_collection("GROUPS")

def group_helper(group) -> dict:
    return {
        "id": str(group["_id"]),
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
    for idUser in group_data['membres']:
        if ObjectId.is_valid(idUser) :
            user = await user_collection.find_one({"_id": ObjectId(idUser)})
            if user : bool = True 
            else : return ErrorResponseModel("An error occurred", 404, "User with id {0} doesn't exist".format(idUser))   
        else : return ErrorResponseModel("An error occurred", 404, "User with id {0} doesn't exist and doesn't has a good format".format(idUser))   
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

# Update a group member with matchings IDs
async def add_user_to_a_group(idGroup: str,idUser: str):
    # Return false if an empty request body is sent.
    group = await group_collection.find_one({"_id": ObjectId(idGroup)})
    if group:
        updated_group = await group_collection.update_one(
            {"_id": ObjectId(idGroup)}, {"$addToSet": { "membres" : idUser } }
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
        "age": user["age"],
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
async def retrieve_movie(id: str) -> dict:
    movie = await movie_collection.find_one({"_id": ObjectId(id)})
    if movie:
        return movie_helper(movie)

# Retrieve all groups present in the database
async def retrieve_movies_2(
        id: str | None,
        title: str | None,
        description: str | None,
        runtimeStr: str | None,
        genreList: List[str] | None,
        contentRating: str | None,
        imDbRating: str | None,
        imDbRatingVotes: int | None,
        metacriticRating: int | None,
        plot: str | None,
        stars: str | None,
        starList: List[StarList] | None,
    ):
    movies = await movie_collection.find(
            {
                '$elemMatch': [
                    { 'value': genreList }
                ]
            }
        )
    return movies

# Retrieve all movies present in the database
async def retrieve_movies():
    movies = []
    async for movie in movie_collection.find():
        movies.append(movie_helper(movie))
    return movies

# Retrieve movies depending parameters
async def retrieve_movies_with_parameters(genreList: str | None, starList: str | None) -> dict:
    movies = []
    parameters = []
    request_genres_value : List[dict] = []
    request_stars_value : List[dict] = []
    request_parameters_mdb : List[dict] = []


    if genreList is not None:
    # Construction de la requête mongodb en fonction du nombre de genre en parametres
        for genre in genreList:
            parameters.append(genre)
            request: dict = { "value" : genre } 
            request_genres_value.append(request)

        #Structure requête mongodb pour filtrer selon les genres en paramètres        
        request_genre_mdb: dict = { "genreList": { "$elemMatch": 
                    {
                        "$or" : 
                            request_genres_value
                    }
                }}
        request_parameters_mdb.append(request_genre_mdb)  

    if starList is not None :
    # Construction de la requête mongodb en fonction du nombre d'acteurs en parametres
        for star in starList:
            parameters.append(star)
            request_stars_value.append(star)   
    #Structure requête mongodb pour filtrer selon les acteurs en paramètres        
        request_star_mdb: dict = { "starList": { "$elemMatch": 
                    {
                        "$or" : 
                            request_stars_value
                    }
                }}

        request_parameters_mdb.append(request_star_mdb)  

    
    if len(request_parameters_mdb) > 1:
        final_request_mdb: dict = { "$or" : request_parameters_mdb}
    else :
        if request_parameters_mdb != [] :
            print(request_parameters_mdb[0])
            final_request_mdb = request_parameters_mdb[0]
            
        else :
            final_request_mdb: dict =  {}

        
    print(final_request_mdb)

    if(parametersAreNull(parameters)) :
        collection = movie_collection.find({})
    else :
        collection = movie_collection.find(final_request_mdb)

    async for movie in movie_collection.find():
        movies.append(movie_helper(movie))
    return movies




# Retrieve all movies by title present in the database
async def retrieve_movie_by_title(title: str | None ) -> dict:
    movies = []
    print(title)
    parameters = [title]
   
    if(parametersAreNull(parameters)) :
        print("cette requete")
        collection = movie_collection.find({})
    else :
        collection = movie_collection.find({'title': title})

    async for movie in collection:
        movies.append(movie_helper(movie))
    return movies

# Retrieve all movies by genre present in the database
async def retrieve_movie_by_genres(genreListe: str | None ) -> dict:
    
    movies = []
    parameters = []
    parameters_request : List[dict] = []

    # Construction de la requête mongodb en fonction du nombre de genre
    for genre in genreListe:
        parameters.append(genre)
        request: dict = { "value" : genre } 
        parameters_request.append(request)

    #Structure requête mongodb pour filtrer selon les genres en paramètres    
    request_genre_mdb: dict = { "genreList": { "$elemMatch": 
                    {
                        "$or" : 
                            parameters_request
                    }
                }}

    if(parametersAreNull(parameters)) :
        collection = movie_collection.find({})
    else :
        collection = movie_collection.find(request_genre_mdb)

    async for movie in collection:
        movies.append(movie_helper(movie))
    return movies


def parametersAreNull(parameters: List[str]):
    bool = True
    for p in parameters:
        if(p != None):
            bool = False
        else: 
            p = " "

    return bool

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
    