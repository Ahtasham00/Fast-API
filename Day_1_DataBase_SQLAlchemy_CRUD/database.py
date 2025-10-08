from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "sqlite:///./test.db"
engine=create_engine(database_url,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()



















"""from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker

database_url="sqlite:///./test.db"
engine=create_engine(database_url,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""










"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)"""