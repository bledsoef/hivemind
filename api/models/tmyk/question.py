from sqlalchemy import ForeignKey, Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from database.config import Base

class Question(Base):
    __tablename__ = "tmyk_questions"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('tmyk_games.id'))
    question = Column(String(1000))
    valid_answers = Column(String(1000))
