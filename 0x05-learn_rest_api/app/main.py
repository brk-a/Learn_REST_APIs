from fastapi import FastAPI, Depends, status, Response
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    """sherpa, this is papa. db testing. do you read me? over."""
    success_msg = {"status": "papa, this is sherpa. reading you loud and clear. over."}
    return success_msg, Response(status_code=status.HTTP_200_OK)
