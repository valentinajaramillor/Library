from typing import Union

from fastapi import FastAPI

from app.routers import libros
from app.database import engine, Base
from app.models.libro_db import LibroDB

app = FastAPI()

app.include_router(libros.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hola"}