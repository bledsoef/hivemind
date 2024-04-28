from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class Guess(Base):
    __tablename__ = "tmyk_guesses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(ForeignKey("tmyk_game_sessions.id"))
    user_id = Column(ForeignKey("users.username"))
    guess = Column(String(1000))

    user = relationship('User', back_populates='tmyk_questions')