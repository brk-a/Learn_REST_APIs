'''
all routes/endpoints that involve users
'''

from fastapi import Depends, status, HTTPException, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponseBase)
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    """create a user"""
    #hash the password for security purposes
    hashed_password = utils.hash_passwd(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}", response_model=schemas.UserResponseBase)
def get_user(id: int, db: Session=Depends(get_db)):
    """fetch one user"""
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user with id {id} was not found')
    return user