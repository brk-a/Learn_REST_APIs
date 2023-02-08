'''
main
'''

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from pydantic import BaseSettings


class Settings(BaseSettings):
    """env variables"""
    database_password: str = "password123"
    database_username: str = "user"
    secret_key: str = "S3cr37kEy"
    


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)