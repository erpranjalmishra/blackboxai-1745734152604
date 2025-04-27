from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend import schemas, models, crud, auth
from backend.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.MedicalRecordOut)
def create_medical_record(medical_record: schemas.MedicalRecordCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    return crud.create_medical_record(db, medical_record)

@router.get("/", response_model=List[schemas.MedicalRecordOut])
def read_medical_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    return crud.get_medical_records(db, skip=skip, limit=limit)

@router.get("/{medical_record_id}", response_model=schemas.MedicalRecordOut)
def read_medical_record(medical_record_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_medical_record = crud.get_medical_record(db, medical_record_id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return db_medical_record

@router.put("/{medical_record_id}", response_model=schemas.MedicalRecordOut)
def update_medical_record(medical_record_id: int, medical_record: schemas.MedicalRecordUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_medical_record = crud.update_medical_record(db, medical_record_id, medical_record)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return db_medical_record

@router.delete("/{medical_record_id}", response_model=schemas.MedicalRecordOut)
def delete_medical_record(medical_record_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_medical_record = crud.delete_medical_record(db, medical_record_id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return db_medical_record
