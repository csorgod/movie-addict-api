from db import db
from sqlalchemy import Column, Integer, Text, DateTime, Boolean

class APIUser(db):
    __tablename__ = 'api_user'

    api_user_id = Column(Integer, primary_key = True)
    username = Column(Text, nullable = False)
    password = Column(Text, nullable = False)
    responsible_cpf = Column(Text, nullable = False)
    responsible_email = Column(Text, nullable = False)
    is_a_robot = Column(Boolean, nullable = False)
    is_active = Column(Boolean, nullable = False)
    created_at = Column(DateTime(timezone = False), nullable = False)
    updated_at = Column(DateTime(timezone = False), nullable = False)
