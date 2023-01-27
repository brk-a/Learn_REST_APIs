'''
Set up all schemas 
(pydantic models)
used by the API
'''

from pydantic import BaseModel, EmailStr
from datetime import datetime


# class Post(BaseModel):
#     """ pydantic schema of a post"""
#     title: str
#     content: str
#     published: bool = True


class PostBase(BaseModel):
    """ pydantic schema of a post"""
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    """create a post: pydantic schema"""
    pass


class PostUpdate(PostBase):
    """update a post: pydantic schema"""
    pass


class PostResponseBase(PostBase):
    """pydantic schema of a response from `/posts` endpoint"""
    #id: int
    created_at: datetime

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True


class UserBase(BaseModel):
    """pydantic schema of a user"""
    email: EmailStr
    password: str
    created_at: datetime


class UserCreate(UserBase):
    """create a user: pydantic schema"""
    pass


class UserResponseBase(UserBase):
    """pydantic schema of a response from `/users` endpoint"""
    email: EmailStr
    created_at: datetime

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True