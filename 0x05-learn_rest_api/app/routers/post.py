'''
all routes/endpoints that involve posts
'''

from fastapi import Depends, status, Response, HTTPException, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/posts", tags=['Posts'])


@router("/sqlalchemy")
def test_posts(db: Session=Depends(get_db)):
    """sherpa, this is papa. db testing. do you read me? over."""
    success_msg = {"status": "papa, this is sherpa. reading you loud and clear. over."}
    return success_msg, Response(status_code=status.HTTP_200_OK)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponseBase)
def create_post(post: schemas.PostCreate, db: Session=Depends(get_db)):
    """create a post"""
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/", response_model=List[schemas.PostResponseBase])
def get_posts(db: Session=Depends(get_db)):
    """fetch all posts"""
    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", response_model=schemas.PostResponseBase)
def get_post(id: int, db: Session=Depends(get_db)):
    """fetch one post"""
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id {id} was not found')
    return post


@router.put("/{id}", response_model=schemas.PostResponseBase)
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
    return updated_post      


@router.delete("/{id}", response_model=schemas.PostResponseBase)
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