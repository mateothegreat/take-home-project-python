from typing import Optional
from typing import List
from uuid import uuid4
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db

# Patient
@app.post("/patients/", response_model=List[schemas.PatientModel])
def create_patient(patients: List[schemas.PatientModel], db: Session = Depends(get_db)):
    for patient in patients:
        db_patient = crud.get_patient_by_name(db, patient.name, patient.id)
        if db_patient:
            raise HTTPException(status_code=400, detail=f'Patient {patient.name} already registered')        
        db_patient=crud.create_patient(db=db, patient= patient)
    return patients

@app.get("/patients/", response_model=List[schemas.Patient])
def list_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.get("/patients/next", response_model=schemas.Patient)
def list_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patient_next(db, skip=skip, limit=limit)
    return patients

@app.get("/patients/next/list", response_model=List[schemas.Patient])
def list_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patient_next_list(db, skip=skip, limit=limit)
    return patients


@app.get("/patient/{patient_id}", response_model=schemas.Patient)
def list_patient(patient_id: str, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.delete("/patient/{patient_id}", response_model=schemas.PatientDelete)
def erase_patient(patient_id: str, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.delete_patient(db,patient_id)

#endPatient

#users

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# endUsers

#defaults test

@app.get("/")
async def read_root():
    return {"Hi Folks": " This is a challenge ApiDocOffice!",
            "Author": "Maprigo",
            "Comments": "I assumed that the doctor had the office at latitude 0 and longitude 0. (to get the distance, I calculate the vector) distance ^ 2 = longitude ^ 2 + latitude ^ 2.",
            "Filters": "The first filter is the attendance ratio,second filter is the distance,third the time of atendance" }