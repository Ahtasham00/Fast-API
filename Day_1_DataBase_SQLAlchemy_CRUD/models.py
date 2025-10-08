from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Users(Base):
  __tablename__="users"
  name=Column(String,nullable=False)
  email=Column(String,unique=True,nullable=False)
  id=Column(Integer,primary_key=True,autoincrement=True)




















"""from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)




"""
















"""from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)"""