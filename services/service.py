from sqlalchemy.orm import Session
import schemas
import models
from exceptions import ItemNotFound
from models import User, New


class UserService:
    @staticmethod
    def create_user(db: Session, new_user: schemas.CreateUser):
        new_user = models.User(**new_user.dict())
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def update(db: Session, obj: schemas.UpdateUser, obj_id: int) -> models.User:
        db_obj = db.query(models.User).get(obj_id)  # noqa
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def get_user(db: Session, obj_id: int) -> models.User:
        db_obj = db.query(models.User).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def delete_user(db: Session, obj_id: int):
        db_user = db.query(models.User).get(obj_id)
        if db_user:
            db.delete(db_user)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound


class NewsService:
    @staticmethod
    def create_news(db: Session, new_news: schemas.CreateNews):
        new_user = models.New(**new_news.dict())
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def update(db: Session, obj: schemas.UpdateNews, obj_id: int) -> models.New:
        db_obj = db.query(models.New).get(obj_id)  # noqa
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def get_news(db: Session, obj_id: int) -> models.New:
        db_obj = db.query(models.New).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def delete_news(db: Session, obj_id: int):
        db_news = db.query(models.New).get(obj_id)
        if db_news:
            db.delete(db_news)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound


class CommentsService:
    @staticmethod
    def create_comment(db: Session, new_comment: schemas.CreateComment):
        comment_user = models.Comment(**new_comment.dict())
        db.add(comment_user)
        db.commit()
        return comment_user

    @staticmethod
    def update(db: Session, obj: schemas.UpdateComment, obj_id: int) -> models.Comment:
        db_obj = db.query(models.Comment).get(obj_id)  # noqa
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def get_comment(db: Session, obj_id: int) -> models.Comment:
        db_obj = db.query(models.Comment).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def delete_comment(db: Session, obj_id: int):
        db_comment = db.query(models.Comment).get(obj_id)
        if db_comment:
            db.delete(db_comment)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound
