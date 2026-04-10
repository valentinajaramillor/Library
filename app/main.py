from typing import Union

from fastapi import FastAPI
from app.routers import libros

app = FastAPI()

app.include_router(libros.router)

@app.get("/")
async def root():
    return {"message": "Hola"}