'''
main
'''

from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app("/sqlalchemy")
def test_posts(db: Session=Depends(get_db)):
    """sherpa, this is papa. db testing. do you read me? over."""
    success_msg = {"status": "papa, this is sherpa. reading you loud and clear. over."}
    return success_msg, Response(status_code=status.HTTP_200_OK)


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session=Depends(get_db)):
    """create a post"""
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@app.get("/posts")
def get_posts(db: Session=Depends(get_db)):
    """fetch all posts"""
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.get("/posts/{id}")
def get_post(id: int, db: Session=Depends(get_db)):
    """fetch one post"""
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id {id} was not found')
    return {"post_detail": post}


@app.put("/posts/{id}")
def update_post(id: int, post: schemas.PostUpdate, db: Session=Depends(get_db)):
    """update one post"""
    post_query = db.query(models.Post).filter(models.Post.id ==  id)
    post_data = post_query.first()
    if not post_data:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id {id} was not found')
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    updated_post = post_query.first()
    return {"updated_post": updated_post}       


@app.delete("/posts/{id}")
def delete_post(id: int, db: Session=Depends(get_db)):
    """delete one post"""
    post_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = post_query.first()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id {id} was not found')
    db.delete(synchronize_session=False)
    db.commit()
    return {"deleted_post": deleted_post}, Response(status_code=status.HTTP_204_NO_CONTENT)