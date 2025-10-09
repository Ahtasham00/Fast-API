from fastapi import FastAPI,Depends
from schema import UserWrite,UserRead,Login
from sqlalchemy.orm import Session
from database import get_db
from models import Users

#For Password Encryption we are going to use passlib
#Hour 1
from passlib.context import CryptContext
#For JWT Token Authentication we are going to use pyJWT
#Hour 2
import jwt
from datetime import datetime,timedelta
#Hour 3
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from fastapi.security import APIKeyHeader
jwt_token = APIKeyHeader(name="Authorization")




secret_key="mysecretkey"
expiry_time=30 #minutes
Algorithm="HS256"
def get_jwt_token(data:dict):
    to_encode=data.copy()
    #to_encode.update({"exp":datetime.utcnow()+timedelta(minutes=expiry_time)})
    expiry=datetime.utcnow()+timedelta(expiry_time )
    to_encode.update({"exp":expiry})
    encoded_jwt=jwt.encode(to_encode,secret_key,algorithm=Algorithm)
    return encoded_jwt



app=FastAPI()

context=CryptContext(schemes=["bcrypt"],deprecated="auto")


@app.post("/users/signup",response_model=UserRead)
def  register_user(user:UserWrite,db:Session=Depends(get_db)):
    print("==========================================")
    print(user.password)
    hash_password=context.hash(user.password)
    user_detail=Users(name=user.name,email=user.email,password=hash_password)
    db.add(user_detail)
    db.commit()
    db.refresh(user_detail)
    return user_detail


@app.get("/users/me")
def get_me(token=Depends(jwt_token),db:Session=Depends(get_db)):
 token = token.replace("Bearer ", "")
 try:
  token_data=jwt.decode(token,secret_key,algorithms=[Algorithm])
  token_email=token_data.get("sub")
  if token_email is None:
   return {"error":"Invalid Token"}
 except ExpiredSignatureError:
    return {"error":"Token Expired"}
 except InvalidTokenError:
    return {"error":"Invalid Token"}
 user_detail=db.query(Users).filter(Users.email==token_email).first()
 return user_detail



@app.get("/users/{user_id}",response_model=UserWrite)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(Users).filter(Users.id==user_id).first()
    return user

@app.post("/login")
def login(credentials:Login,db:Session=Depends(get_db)):
    user=db.query(Users).filter(Users.email==credentials.email).first()
    if not user:
        return {"error":"Invalid Credentials"}
    if not context.verify(credentials.password,user.password):
        return {"error":"Invalid Password"}
    access_token=get_jwt_token(data={"sub":user.email})
    return access_token

