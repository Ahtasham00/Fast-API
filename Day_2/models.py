from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class Users(Base):
  __tablename__="users"
  name=Column(String,nullable=False)
  email=Column(String,unique=True,nullable=False)
  password=Column(String,nullable=False)
  id=Column(Integer,primary_key=True,autoincrement=True)

