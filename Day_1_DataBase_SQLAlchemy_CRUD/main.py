from fastapi import FastAPI,Depends
from schema import UserWrite,UserRead
from sqlalchemy.orm import session
from database import get_db
from models import Users
app=FastAPI()



@app.post("/users/adduser",response_model=UserRead)
def adduser(user:UserWrite,db:session=Depends(get_db)):
    user_info=Users(name=user.name,email=user.email)
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info   

@app.get("/users/",response_model=list[UserRead])
def getusers(db:session=Depends(get_db)):
    users=db.query(Users).all()
    return users


@app.get("/users/{id}",response_model=UserRead)
def getUserById(id:int,db:session=Depends(get_db)):
    user=db.query(Users).filter(Users.id==id).first()   
    return user

@app.get("/users",response_model=UserRead)
def getUserById(userId:int,db:session=Depends(get_db)):
    user=db.query(Users).filter(Users.id==userId).first()   
    return user



 



















"""
from models import Base, User
from database import SessionLocal,engine
from fastapi import FastAPI

app=FastAPI()


Base.metadata.create_all(bind=engine)
db=SessionLocal()


@app.get("/users/")
def read_users():
 users=db.query(User).all()
 return users

"""














"""from models import Base, User
from database import SessionLocal,engine

Base.metadata.create_all(bind=engine)
db=SessionLocal()
new_user=User(name="Ahmed",email="Ahmed1@gmail.com")
db.add(new_user)
db.commit()
db.refresh(new_user)
print("New user added:",new_user.id)
users=db.query(User)
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
db.close()

"""