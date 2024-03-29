'''
Set up all schemas 
(pydantic models)
used by the API
as endpoints
'''

from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


# class Post(BaseModel):
#     """ pydantic schema of a post"""
#     title: str
#     content: str
#     published: bool = True


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
    id: int
    created_at: datetime
    owner_id: int
    owner: UserBase

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True


class PostResponseJoinVote(PostBase):
    """pydantic schema of the table made by joining `Post` and `Vote`"""
    Post: PostResponseBase
    votes: int

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True


class LoginBase(BaseModel):
    """pydantic schema of a request to `/login` endpoint"""
    email: EmailStr
    password: str

    # class Config:
    #     """tells pydantic to read data even if it is not a `dict`"""
    #     orm_mode = True


class Token(BaseModel):
    """pydantic schema of a JWT  from `/login` endpoint"""
    access_token: str
    token_type: str

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True


class TokenData(BaseModel):
    """pydantic schema of data in a JWT from `/login` endpoint"""
    id: Optional[str] =  None

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True


class Vote(BaseModel):
    """pydantic schema of data to be sent from `/vote` endpoint"""
    post_id: int
    vote_dir: conint(ge=0,le=1)
