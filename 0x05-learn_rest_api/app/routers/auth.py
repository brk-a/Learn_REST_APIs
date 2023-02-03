'''
use JWT to authenticate users
'''

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import Token
from ..models import User
from ..utils import verify
from ..oauth2 import create_access_token

router = APIRouter(tags='Authentication')


@router.post("/login", response_model=Token)
def login(user_creds: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    """ authenticate a user """
    user = db.query(User).filter(User.email == user_creds.username).first()
    #OAuth2PasswordRequestForm does not give a f; it returns a dict viz:
    #{
    #   "username": "sample text",
    #   "password": "more sample text"
    #}

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid credentials')
    
    if not verify(user_creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid credentials')

    #create a token
    access_token = create_access_token({"user_id": user.id})
    #return token
    return {"access_token": access_token, "token_type": "bearer"}
