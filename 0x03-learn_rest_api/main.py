from fastapi import FastAPI
from fastapi.params import Body
# from box import Box #use dot notation to access values in a dictionary w/o using the class below
from pydantic import BaseModel
from typing import Optional


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


@app.get('/')
async def root():
    return {"message": "Hello, world!"}


@app.get('/posts')
def get_posts():
    return {"data": "This is a sample post"}


@app.post('/createpost')
def create_post(new_post: Post):
    # new_post = AttributeDict(new_post) #IFF you use class AttributeDict
    # new_post = Box(new_post) #IFF you use Box
    print(new_post)
    return {
        "message": "Post created successfully",
        "title": f"title: {new_post.title}", #instead of new_post['title']
        "content": f"content: {new_post.content}", #instead of new_post['content']
        "published": f"published: {new_post.published}",
        "rating": f"rating: {new_post.rating}"
    }
