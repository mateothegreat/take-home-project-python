from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Patient(Base):

    __tablename__ = "patient"


    id = Column(String, primary_key=True)
    name = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    age = Column(Integer)
    appointmentsAttended = Column(Integer)
    appointmentsMissed = Column(Integer)
    averageReplyTime = Column(Integer)
    is_active = Column(Boolean, default=True)
    ratio=Column(Integer)
    distance=Column(Float)