from sqlalchemy import create_engine, Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class JsonData(Base):
    __tablename__ = 'sensor_data'
    
    id = Column(Integer, primary_key=True)
    data = Column(JSON)

# Create an SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///instance/database.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
