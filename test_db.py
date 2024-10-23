from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class User(Base):  # A simple model
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

engine_url = f'mysql+pymysql://{os.getenv("HBNB_MYSQL_USER")}:{os.getenv("HBNB_MYSQL_PWD")}@{os.getenv("HBNB_MYSQL_HOST")}/{os.getenv("HBNB_MYSQL_DB")}'
engine = create_engine(engine_url, echo=True)  # echo=True will print the SQL queries

Base.metadata.create_all(engine)  # Create the table

Session = sessionmaker(bind=engine)
session = Session()

# Try adding a user
new_user = User(name="Test User")
session.add(new_user)
session.commit()