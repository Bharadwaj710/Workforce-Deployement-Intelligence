from fastapi import APIRouter
from app.schemas.employee import EmployeeProfile

router=APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/employee")
def create_employee(employee:EmployeeProfile):
    return{
        "message":"employee profile sucesfully created",
        "employee":employee
    }