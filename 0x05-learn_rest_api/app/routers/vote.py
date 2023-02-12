'''
all routes/endpoints that involve votes
'''

from fastapi import Depends, status, Response, HTTPException, APIRouter
from .. import schemas, oauth2, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/vote", tags=['Vote'])

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote, db: Session=Depends(database.get_db), get_current_user: int=Depends(oauth2.get_current_user)):
    """upvote or downvote a post"""
    vote_query = db.query(models.Vote).filter(vote.post_id == models.Vote.post_id,
        get_current_user.id == models.Vote.user_id)
    found_vote = vote_query.first()
    if vote.vote_dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail=f"user {get_current_user.id} already liked post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=vote.user_id)
        db.add(new_vote)
        db.commit()

        return new_vote, {"message": "vote added successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "vote deleted successfully"}, Response(status_code=status.HTTP_204_NO_CONTENT)