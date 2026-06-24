from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from db_conn.db_manager import Base


class UserTest(Base):
    __tablename__ = "users_test"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

