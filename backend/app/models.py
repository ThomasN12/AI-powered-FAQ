from sqlalchemy import Column, Integer, String, ARRAY, DateTime
from datetime import datetime
from .database import Base

class FAQ(Base):
    __tablename__ = "faqs"
    
    id = Column(Integer, primary_key=True)
    question = Column(String)
    question_body = Column(String)
    answer = Column(String)
    related_questions = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)