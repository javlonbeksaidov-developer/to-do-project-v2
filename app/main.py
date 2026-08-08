from fastapi import FastAPI

from app.database import create
from app.routes import router

app = FastAPI()

create()

app.include_router(router)
