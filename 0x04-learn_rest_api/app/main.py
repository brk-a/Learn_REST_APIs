import psycopg2
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import os


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

try: 
    conn = psycopg2.connect(host="localhost", database="fastapi", user=user_name, password=password)
    cur = conn.cursor()
except:
    raise
else:
    pass
finally:
    pass