from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


user = "postgres"
password = "1234"
host = "127.0.0.1"
dataBase = "blog"

DATABASE_URI = f"postgresql://{user}:{password}@{host}/{dataBase}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()