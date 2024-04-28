from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String(50), primary_key=True, index=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    # password = Column(String(50))

    # classParticipants = relationship('ClassParticipant', back_populates='user')
    # classInstructors = relationship('ClassInstructor', back_populates='user')
    # classResources = relationship('ClassResource', back_populates='user')