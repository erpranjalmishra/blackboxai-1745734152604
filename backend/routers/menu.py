from fastapi import APIRouter, Depends
from backend.auth import get_current_active_user
from backend.models import User

router = APIRouter()

menus = {
    "admin": [
        {"name": "Dashboard", "url": "/admin-dashboard"},
        {"name": "User Management", "url": "/user-role-management"},
        {"name": "Reports", "url": "/reports-and-analytics"},
        {"name": "Settings", "url": "/settings"},
    ],
    "doctor": [
        {"name": "Dashboard", "url": "/doctor-dashboard"},
        {"name": "Patient Management", "url": "/patient-management"},
        {"name": "Appointment Management", "url": "/appointment-management"},
        {"name": "Medical Records", "url": "/medical-records"},
    ],
    "patient": [
        {"name": "Dashboard", "url": "/patient-dashboard"},
        {"name": "Appointments", "url": "/appointment-management"},
        {"name": "Medical Records", "url": "/medical-records"},
        {"name": "Billing", "url": "/billing-and-invoicing"},
    ],
    "staff": [
        {"name": "Dashboard", "url": "/staff-dashboard"},
        {"name": "Inventory", "url": "/inventory-management"},
        {"name": "Billing", "url": "/billing-and-invoicing"},
        {"name": "Reports", "url": "/reports-and-analytics"},
    ],
}

@router.get("/menu")
def get_menu(current_user: User = Depends(get_current_active_user)):
    role = current_user.role if current_user else "patient"
    return menus.get(role, menus["patient"])
