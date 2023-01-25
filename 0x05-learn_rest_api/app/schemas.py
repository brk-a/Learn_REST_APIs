'''
Set up all schemas 
(pydantic models)
used by the API
'''

from pydantic import BaseModel

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
