from app.schemas.employee import EmployeeProfile

def create_employee_profile(employee:EmployeeProfile):
    return{
        "message":"employee profile sucesfully created",
        "employee":employee
    }