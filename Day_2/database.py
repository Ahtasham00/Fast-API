from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from models import Base,Users

database_url = "sqlite:///./test.db"
engine=create_engine(database_url,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
#Base.metadata.create_all(bind=engine)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()