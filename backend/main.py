from fastapi import FastAPI
import os
from app.api.emplyee_router import router as employee_router
from app.core.config import settings

app= FastAPI(
    title=settings.app_name
)


@app.get("/")
def home():
    return{
        "application":settings.app_name,
        "environment":settings.environment,
        "message":"Welcome to WDIP"
    }

@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }

app.include_router(employee_router)
