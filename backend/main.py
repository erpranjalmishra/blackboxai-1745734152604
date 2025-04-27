from fastapi import FastAPI
from backend.routers import users, patients, doctors, appointments, medical_records, inventory, invoices, menu, otp, notifications, news, weather, ai_health
from backend.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(medical_records.router, prefix="/medical_records", tags=["medical_records"])
app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
app.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
app.include_router(menu.router, prefix="/menu", tags=["menu"])
app.include_router(otp.router, prefix="/otp", tags=["otp"])
app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
app.include_router(news.router, prefix="/news", tags=["news"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
app.include_router(ai_health.router, prefix="/ai_health", tags=["ai_health"])
