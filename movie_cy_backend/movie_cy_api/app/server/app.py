from fastapi import FastAPI
from typing import Optional
from app.server.routes.user import router as UserRouter

from app.server.routes.group import router as GroupRouter

app = FastAPI()

app.include_router(GroupRouter, tags=["Group"], prefix="/group")
app.include_router(UserRouter, tags=["User"], prefix="/user")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

