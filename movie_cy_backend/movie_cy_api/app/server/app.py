from fastapi import FastAPI
from typing import Optional

from app.server.routes.group import router as GroupRouter

app = FastAPI()

app.include_router(GroupRouter, tags=["Group"], prefix="/group")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

