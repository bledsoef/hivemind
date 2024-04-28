from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class User(Base):
    __tablename__ = "users"
    
    username = Column(String(50), primary_key=True, index=True)
    email = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))

    created_games = relationship('Game', back_populates="creator", foreign_keys="[Game.user_id]")
