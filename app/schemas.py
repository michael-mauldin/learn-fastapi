from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


# User models
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Request models
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


# Response models
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # tell Pydantic we are using an ORM model
    class Config:
        orm_mode = True


class PostOut(PostBase):
    Post: Post
    votes: int


# Authentication
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None


# Vote models
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
