from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = "root"
password = "1234"
host = "localhost"
dataBase = "blog"

DATABASE_URI = f"mysql://{user}:{password}@{host}/{dataBase}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

