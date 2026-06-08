from fastapi import APIRouter
from app.schemas.employee import EmployeeProfile
from app.services.employee_service import (create_employee_profile)

router=APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/employee")
def create_employee (employee:EmployeeProfile):
    return create_employee_profile(employee)