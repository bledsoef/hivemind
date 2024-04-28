from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class Game(Base):
    __tablename__ = "tmyk_games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000))
    user_id = Column(String(50), ForeignKey("users.username"))

    creator = relationship("User", back_populates="created_games", foreign_keys=[user_id])