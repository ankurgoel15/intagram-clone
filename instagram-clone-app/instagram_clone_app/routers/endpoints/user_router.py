from  fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from instagram_clone_app.db.database import get_db
from instagram_clone_app.services import db_user
from instagram_clone_app.models.user_models import UserBase, UserDisplay

router = APIRouter()


@router.post("/", response_model=UserDisplay, status_code= status.HTTP_201_CREATED)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    try:
        user = db_user.create_user(request, db)
        return {"User Created Successfully": user}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=f"Error occured while creating a user")