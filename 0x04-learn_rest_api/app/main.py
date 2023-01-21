import psycopg2
import os
import time
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor


class Post(BaseModel):
    """class Post"""
    title: str
    content: str
    published: bool = True

app = FastAPI()

if os.access("../.env", os.R_OK):
    with open('.env') as f:
        user_name = f[0]
        password = f[1]

while True:
    try: 
        conn = psycopg2.connect(host="localhost", database="fastapi", user=user_name,
            password=password, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print(f'Connection created successfully')
        break
    except Exception as err:
        print(f'Connection was not created')
        print(f'Error is... {err}')
        time.sleep(2)


@app.get("/posts")
def get_posts():
    """fetch all posts"""
    cur.execute(""" SELECT * FROM posts """)
    posts = cur.fetchall()
    return {"data": posts}


@app.post("/posts/{id}")
def create_post(post: Post):
    """create a post"""
    cur.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING """,
        (post.title, post.content, post.published))
    new_post = cur.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    """fetch one post"""
    cur.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id {id} was not found')
    return {"data": post}