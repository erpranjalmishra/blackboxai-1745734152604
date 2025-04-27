from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Optional[str] = "user"
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    is_active: Optional[bool]

class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Patient Schemas
class PatientBase(BaseModel):
    name: str
    age: Optional[int]
    gender: Optional[str]
    contact: Optional[str]
    address: Optional[str]
    profile_picture: Optional[str]

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    contact: Optional[str]
    address: Optional[str]
    profile_picture: Optional[str]

class PatientOut(PatientBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Doctor Schemas
class DoctorBase(BaseModel):
    name: str
    specialization: Optional[str]
    availability: Optional[str]
    schedule: Optional[str]

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    name: Optional[str]
    specialization: Optional[str]
    availability: Optional[str]
    schedule: Optional[str]

class DoctorOut(DoctorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Appointment Schemas
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    datetime: datetime
    status: Optional[str] = "pending"

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int]
    doctor_id: Optional[int]
    datetime: Optional[datetime]
    status: Optional[str]

class AppointmentOut(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Medical Record Schemas
class MedicalRecordBase(BaseModel):
    patient_id: int
    record_type: Optional[str]
    description: Optional[str]
    file_url: Optional[str]
    date: Optional[datetime]

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordUpdate(BaseModel):
    record_type: Optional[str]
    description: Optional[str]
    file_url: Optional[str]
    date: Optional[datetime]

class MedicalRecordOut(MedicalRecordBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Inventory Schemas
class InventoryBase(BaseModel):
    item_name: str
    quantity: Optional[int] = 0
    expiry_date: Optional[datetime]
    item_type: Optional[str]

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[datetime]
    item_type: Optional[str]

class InventoryOut(InventoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Invoice Schemas
class InvoiceBase(BaseModel):
    patient_id: int
    amount: float
    payment_status: Optional[str] = "pending"
    insurance_claim: Optional[bool] = False

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    amount: Optional[float]
    payment_status: Optional[str]
    insurance_claim: Optional[bool]

class InvoiceOut(InvoiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Emergency Alert Schemas
class EmergencyAlertBase(BaseModel):
    message: str
    priority: Optional[str] = "low"
    status: Optional[str] = "active"

class EmergencyAlertCreate(EmergencyAlertBase):
    pass

class EmergencyAlertUpdate(BaseModel):
    message: Optional[str]
    priority: Optional[str]
    status: Optional[str]

class EmergencyAlertOut(EmergencyAlertBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# Message Schemas
class MessageBase(BaseModel):
    sender_id: int
    receiver_id: int
    content: str
    read: Optional[bool] = False

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    content: Optional[str]
    read: Optional[bool]

class MessageOut(MessageBase):
    id: int
    timestamp: datetime

    model_config = {"from_attributes": True}
