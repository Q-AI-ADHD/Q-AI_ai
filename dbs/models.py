from sqlalchemy import Column, Integer, String, Text
from dbs.db import Base

class Quest(Base):
    __tablename__ = 'questions'

    id = Column(String, primary_key=True, index = True)
    subject = Column(String, nullable = False)
    level = Column(String, nullable = False)
    question = Column(String, nullable = False)