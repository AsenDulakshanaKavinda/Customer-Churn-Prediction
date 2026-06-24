import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()


Base = declarative_base()


class DatabaseManager:
    _instance: Optional["DatabaseManager"] = None

    engine: Engine
    SessionLocal: sessionmaker[Session]

    def __new__(cls):
        if cls._instance is None:
            print("Initializing SQLAlchemy Engine...")
            cls._instance = super().__new__(cls)

        DATABASE_URL = os.getenv(
            "DATABASE_URL", "postgresql+psycopg://admin:password@localhost:5432/DB"
        )
        print(DATABASE_URL)

        cls._instance.engine = create_engine(
            DATABASE_URL,
            pool_size=5,
            max_overflow=10,
        )

        cls._instance.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=cls._instance.engine,
        )

        return cls._instance

    def get_session(self):
        return self.SessionLocal()
