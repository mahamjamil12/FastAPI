from pydantic import BaseModel, Field

class Blog(BaseModel):
    title:str
    content:str




# we can define that which thing we want to show in response and which thing to hide 
class ShowBlog(BaseModel):
    title:str
    class Config():
        orm_mode=True




class User(BaseModel):
    name:str
    email:str
    password: str = Field(min_length=8, max_length=72)