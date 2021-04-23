from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
import models, schemas
import math



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, HTTPExceptionhashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# patient

def get_patient(db: Session, patient_id: str):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def delete_patient(db: Session, patient_id: str):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).delete()
    db.commit()
    return {"Hello": "World yeah!!"}

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_patient_next(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).order_by(desc(models.Patient.ratio),asc(models.Patient.distance),desc(models.Patient.averageReplyTime)).offset(skip).first()

def get_patient_next_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).order_by(desc(models.Patient.ratio),asc(models.Patient.distance),desc(models.Patient.averageReplyTime)).offset(skip).all()


def create_patient(db: Session, patient: schemas.PatientModel):
    hipo=pow(float(patient.location.latitude),2)+pow(float(patient.location.longitude),2)
    distance=math.sqrt(hipo)
    ratioCal=patient.appointmentsAttended * 100/(patient.appointmentsAttended + patient.appointmentsMissed)
    db_patient = models.Patient(id=patient.id,distance=distance, ratio=ratioCal, name=patient.name, age=patient.age, latitude=patient.location.latitude, longitude=patient.location.longitude ,appointmentsAttended=patient.appointmentsAttended, appointmentsMissed=patient.appointmentsMissed, averageReplyTime=patient.averageReplyTime)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return patient.dict()

def get_patient_by_name(db: Session, name: schemas.PatientModel, id: schemas.PatientModel):
    return db.query(models.Patient).filter(models.Patient.name == name and models.Patient.id == id).first()

