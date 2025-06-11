from sqlalchemy.orm.session import Session
from instagram_clone_app.models.user_models import UserBase, UserDisplay
from instagram_clone_app.db.models import DbUser

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()