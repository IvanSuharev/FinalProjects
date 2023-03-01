from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str


class CreateUser(BaseUser):
    created_at: datetime


class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]


class UserInDB(BaseUser):
    id: int

    class Config:
        orm_mode = True


class BaseNews(BaseModel):
    description: str
    user_id: int


class CreateNews(BaseNews):
    created_at: datetime


class UpdateNews(BaseModel):
    description: Optional[str]


class NewsInDB(BaseNews):
    id: int

    class Config:
        orm_mode = True


class BaseComment(BaseModel):
    description: str
    user_id: int
    news_id: int


class CreateComment(BaseComment):
    created_at: datetime


class UpdateComment(BaseModel):
    description: Optional[str]


class CommentInDB(BaseComment):
    id: int

    class Config:
        orm_mode = True


class UsersNewsInDb(BaseModel):
    id: int
    news: list[NewsInDB]

    class Config:
        orm_mode = True


class UsersCommentsInDb(BaseModel):
    id: int
    comments: list[CommentInDB]

    class Config:
        orm_mode = True

