from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Import your SQLAlchemy Base and models

DATABASE_URL = 'postgresql://postgres:ov3E79fqnN0AtV20r0DIALYM2XvwwGYwWqdj5iIrYhJ5c6Kgi3mdzDK5Sp2qDvIP@vkwokco40oo004skkgo8w0w8:5432/postgres'

# Create an engine and bind it to the Base
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

print("Database tables created.")
