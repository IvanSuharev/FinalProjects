from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

import models
import schemas
from database import get_db
from services import UserService, NewsService, CommentsService

user_router = APIRouter(prefix="/user", tags=["user"])
news_router = APIRouter(prefix="/news", tags=["news"])
comment_router = APIRouter(prefix="/comment", tags=["comment"])


@user_router.post("/")
def create_new_user(
    new_user: schemas.CreateUser, db: Session = Depends(get_db)
) -> schemas.UserInDB:
    return UserService.create_user(db=db, new_user=new_user)


@user_router.patch("/<user_id>")
def update_user(
    user_id: int, user: schemas.UpdateUser, db: Session = Depends(get_db)
) -> schemas.UserInDB:
    return UserService.update(db=db, obj=user, obj_id=user_id)


@user_router.get("/get_user/<user_id>")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db=db, obj_id=user_id)


@user_router.get("/get_news_for_user/<user_id>")
def get_my_news(user_id: int, db: Session = Depends(get_db)) -> schemas.UsersNewsInDb:
    news = db.query(models.New).filter(models.New.user_id == user_id)
    return schemas.UsersNewsInDb(id=user_id, news=list(news))


@user_router.get("/get_comments_for_user/<user_id>")
def get_my_comments(
    user_id: int, db: Session = Depends(get_db)
) -> schemas.UsersCommentsInDb:
    comments = db.query(models.Comment).filter(models.Comment.user_id == user_id)
    return schemas.UsersCommentsInDb(id=user_id, comments=list(comments))


@user_router.delete("/delete_user/<user_id>")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db=db, obj_id=user_id)


@news_router.post("/")
def create_new_news(
    new_news: schemas.CreateNews, db: Session = Depends(get_db)
) -> schemas.NewsInDB:
    return NewsService.create_news(db=db, new_news=new_news)


@news_router.patch("/<news_id>")
def update_news(
    news_id: int, user: schemas.UpdateNews, db: Session = Depends(get_db)
) -> schemas.NewsInDB:
    return NewsService.update(db=db, obj=user, obj_id=news_id)


@news_router.get("/get_news/<news_id>")
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    return NewsService.get_news(db=db, obj_id=news_id)


@news_router.delete("/delete_news/<news_id>")
def delete_news_by_id(news_id: int, db: Session = Depends(get_db)):
    return NewsService.delete_news(db=db, obj_id=news_id)


@comment_router.post("/")
def create_new_comment(
    new_comment: schemas.CreateComment, db: Session = Depends(get_db)
) -> schemas.CommentInDB:
    return CommentsService.create_comment(db=db, new_comment=new_comment)


@comment_router.patch("/<comment_id>")
def update_comment(
    comment_id: int, user: schemas.UpdateComment, db: Session = Depends(get_db)
) -> schemas.CommentInDB:
    return CommentsService.update(db=db, obj=user, obj_id=comment_id)


@comment_router.get("/get_comment/<comment_id>")
def get_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return CommentsService.get_comment(db=db, obj_id=comment_id)


@comment_router.delete("/delete_comment/<comment_id>")
def delete_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return CommentsService.delete_comment(db=db, obj_id=comment_id)
