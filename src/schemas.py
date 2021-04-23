from typing import List, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field   



class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = False



class Location(BaseModel):
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    
    

class PatientModel(Location):
    id: str
    name: str
    age: Optional[int] = None
    location: Optional[Location] = None 
    appointmentsAttended: Optional[int] = None
    appointmentsMissed: Optional[int] = None
    averageReplyTime: Optional[int] = None
    ratio: Optional[int] = None
    distance: Optional[float] = None    
    
    
class Patient(Location):
    id: str
    name: Optional[str] = None
    age: Optional[int] = None
    location: Optional[Location] = None 
    appointmentsAttended: Optional[int] = None
    appointmentsMissed: Optional[int] = None
    averageReplyTime: Optional[int] = None
    ratio: Optional[int] = None
    distance: Optional[float] = None
    
    class Config:
        orm_mode = True
        
class PatientDelete(BaseModel):
    pass