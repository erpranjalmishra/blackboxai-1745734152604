from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import schemas, crud, auth
from backend.database import SessionLocal
from backend.utils.email_sender import send_otp_email
import random
import string

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

@router.post("/send-otp")
def send_otp(email: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    otp = generate_otp()
    # Save OTP in DB or cache with expiration (not implemented here)
    send_otp_email(email, otp)
    return {"message": "OTP sent successfully"}

@router.post("/verify-otp")
def verify_otp(email: str, otp: str, db: Session = Depends(get_db)):
    # Verify OTP from DB or cache (not implemented here)
    # For demo, assume OTP is always valid
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
