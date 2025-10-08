from pydantic import BaseModel

class UserWrite(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True




















"""from pydantic import BaseModel

class userCreate(BaseModel):
    name: str
    email: str

class userResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True"""