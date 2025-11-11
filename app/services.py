
from sqlalchemy.orm import Session
from . import models, schemas

class UserService:
    def get_user(self, db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    def create_user(self, db: Session, user: schemas.UserCreate):
        db_user = models.User(email=user.email, name=user.name)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int, user: schemas.UserCreate):
        db_user = self.get_user(db, user_id)
        if db_user:
            db_user.email = user.email
            db_user.name = user.name
            db.commit()
            db.refresh(db_user)
        return db_user

    def delete_user(self, db: Session, user_id: int):
        db_user = self.get_user(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user

user_service = UserService()
