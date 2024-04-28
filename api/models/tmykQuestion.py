from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class TMYKQuestion(Base):
    __tablename__ = "tmyk_questions"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('tmyk.id'))
    name = Column(String(50))
    question = Column(String(50))

    game = relationship('TMYK', back_populates='tmykQuestions')
    user = relationship('User', back_populates='tmykQuestions')