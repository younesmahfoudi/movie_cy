from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional
from app.server.routes.user import router as UserRouter

from app.server.routes.group import router as GroupRouter

from app.server.routes.movie import router as MovieRouteur

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(GroupRouter, tags=["groups"], prefix="/groups")
app.include_router(UserRouter, tags=["users"], prefix="/users")
app.include_router(MovieRouteur, tags=["movies"], prefix="/movies")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

