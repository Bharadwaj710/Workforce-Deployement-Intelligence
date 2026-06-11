from fastapi import FastAPI
import os
from app.api.emplyee_router import router as employee_router
from app.core.config import settings
from app.api.predictor_router import router as predictor_router

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
app.include_router(predictor_router)