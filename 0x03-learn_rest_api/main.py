'''
Docstring will be completed later
'''

from fastapi import FastAPI
from fastapi.params import Body
# from box import Box #use dot notation to access values in a dictionary w/o using the class below
from pydantic import BaseModel
from typing import Optional
from random import randrange


# class AttributeDict(dict):
#     """use dot notation to access values in a dictionary"""
#     __getattr__ = dict.__getitem__
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__


class Post(BaseModel):
    """ Schema for a post"""
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


app = FastAPI()
all_posts = [
    {'title': 'Title 0', 'content': 'Content 0', 'pseudo_id': 0},
    {'title': 'Title 1', 'content': 'Content 1', 'pseudo_id': 1}
]


@app.get('/')
async def root():
    """display `Hello World` message"""
    return {'message': 'Hello, World'}


@app.get('/posts')
def get_posts():
    """ fetch all posts"""
    return {"data": all_posts}


@app.post('/posts')
def create_post(post: Post):
    """create a post"""
    # posts = AttributeDict(posts) #IFF you use class AttributeDict
    # posts = Box(posts) #IFF you use Box
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000000000)
    all_posts.append(post_dict)
    # return {
    #     "message": "Post created successfully",
    #     "title": f"title: {post.title}", #instead of post['title']
    #     "content": f"content: {post.content}", #instead of post['content']
    #     "published": f"published: {post.published}",
    #     "rating": f"rating: {post.rating}"
    # }
    return{"data": post_dict}


@app.get('posts/{id}')
def get_post(id: int):
    """fetch one post by id"""
    return {"post_detail": f'Here is post {id}'}
