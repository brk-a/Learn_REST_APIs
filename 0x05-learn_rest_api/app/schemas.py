'''
Set up all schemas 
(pydantic models)
used by the API
'''

from pydantic import BaseModel
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


class ResponseBase(PostBase):
    """pydantic schema of a response"""
    #id: int
    created_at: datetime

    class Config:
        """tells pydantic to read data even if it is not a `dict`"""
        orm_mode = True