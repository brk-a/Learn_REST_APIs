'''
use JWT to authenticate users
'''

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import LoginBase
from ..models import User
from ..utils import verify

router = APIRouter(tags='Authentication')


@router.post("/login")
def login(user_creds: LoginBase, db: Session=Depends(get_db)):
    """ authenticate a user """
    user = db.query(User).filter(User.email == user_creds.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Invalid credentials')
    
    if not verify(user_creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Invalid credentials')

    #create a token

    #return token
    return {"token": "example token"}
