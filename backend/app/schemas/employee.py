from pydantic import BaseModel
from typing import List

class EmployeeProfile(BaseModel):
    name:str
    experience_years:int
    current_role:str
    skills: List[str]
