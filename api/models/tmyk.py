from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class TMYK(Base):
    __tablename__ = "tmyk"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    user = relationship('User', back_populates='tmyk')