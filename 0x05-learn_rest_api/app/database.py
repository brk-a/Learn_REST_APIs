from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

if os.access("../.env", os.R_OK):
    with open('.env') as f:
        USER_NAME = f[0]
        PASSWORD= f[1]
        HOSTNAME= f[2]
        DATABASE_NAME= f[3]

SQLALCHEMY_DATABASE_URL = f'postgresql://{USER_NAME}:{PASSWORD}@{HOSTNAME}/{DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """get db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        