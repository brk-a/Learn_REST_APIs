'''
oauth

create JWt tokens
'''

from jose import JWTError, jwt
from subprocess import Popen, PIPE
from datetime import datetime, timedelta


#SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
with Popen("openssl rand -hex 32", stdout=PIPE, shell=True) as secret_key:
    SECRET_KEY = secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    """ create a JSON Web Token"""
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
