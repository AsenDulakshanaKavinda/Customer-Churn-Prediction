import os
from dotenv import load_dotenv; load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Initializing SQLAlchemy Engine...")
            cls._instance = super().__new__(cls)

        DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://admin:password@localhost:5432/DB")
        print(DATABASE_URL)

        cls._instance.engine = create_engine(
            DATABASE_URL, 
            pool_size = 5, 
            max_overflow = 10,
        )

        cls._instance.SessionLocal = sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = cls._instance.engine,
        )

        return cls._instance
    
    def get_session(self):
        return self.SessionLocal()


