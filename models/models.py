from sqlalchemy import Text, Column, Integer, DateTime, ForeignKey, Date
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())

    news = relationship("New")
    comments = relationship("Comment")


class New(Base):
    __tablename__ = "news_for_user"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"))

    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"))

    news_id = Column(Integer, ForeignKey("news_for_user.id"))
