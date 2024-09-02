from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the connection string to your PostgreSQL database
DATABASE_URL = 'postgresql://postgres:ov3E79fqnN0AtV20r0DIALYM2XvwwGYwWqdj5iIrYhJ5c6Kgi3mdzDK5Sp2qDvIP@vkwokco40oo004skkgo8w0w8:5432/postgres'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a base class for declarative models
Base = declarative_base()

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
