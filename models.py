from datetime import datetime

from database import Base
from sqlalchemy import Column, Integer, String, Date, Boolean

def _get_date():
    return datetime.now()

class Users(Base):
    __tablename__ = 'users'
    is_admin = Column(Boolean)
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    create_at = Column(Date, default=_get_date)
    hashed_password = Column(String)

