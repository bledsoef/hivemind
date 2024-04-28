from sqlalchemy import ForeignKey, Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from database.config import Base

class QuestionClue(Base):
    __tablename__ = "tmyk_question_clues"

    id = Column(Integer, primary_key=True, index=True)
    index = Column(Integer)
    question_id = Column(Integer, ForeignKey('tmyk_questions.id'))
    clue = Column(String(1000))