from fastapi import FastAPI
import os
from app.api.emplyee_router import router as employee_router

app=FastAPI(
    title="Workforce Deployement Intelligence Platform"
)

@app.get("/")
def home():
    return{
        "message":"Welcome to WDIP"
    }

@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }

app.include_router(employee_router)
