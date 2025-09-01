from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from sqlalchemy.sql import func
from datetime import datetime

# ChatHistory Table

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    message = Column(Text, nullable=False)  
    response = Column(Text, nullable=False)  
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)





