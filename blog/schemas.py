from pydantic import BaseModel, Field
from typing import Optional

class BlogBase(BaseModel):
    title:str
    content:str


class Blog(BlogBase):
    class Config():
       from_attributes =True
class User(BaseModel):
    name:str
    email:str
    password: str


class ShowUser(BaseModel):
    name:str
    email:str
    # blogs:List

    class Config():
       from_attributes =True


# we can define that which thing we want to show in response and which thing to hide 
class ShowBlog(BaseModel):
    title:str
    content:str
    creator: Optional[ShowUser] = None
    class Config():
       from_attributes =True