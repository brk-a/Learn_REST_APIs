'''
oauth

create JWTs
'''

from jose import JWTError, jwt
# from subprocess import Popen, PIPE
from datetime import datetime, timedelta
from .schemas import TokenData
from .database import get_db
from .models import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# with Popen("openssl rand -hex 32", stdout=PIPE, shell=True) as secret_key:
#     SECRET_KEY = secret_key
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    """ create a JSON Web Token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    """verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id : str = payload.get("user_id")

        if not id:
            raise credentials_exception
        
        token_data = TokenData(id=id)
    except JWTError as e:
        print(e)
        raise credentials_exception
    except AssertionError as e:
        print(e)
        raise credentials_exception

    return token_data


def get_current_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
    """fetch the current user"""
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f'Could not validate credentials', headers={"WWW-Authenticate": "Bearer" })

    token_data = verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token_data.id).first()

    return user 