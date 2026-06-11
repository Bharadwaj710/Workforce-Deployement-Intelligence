from pydantic import BaseModel


class PredictorRequest(BaseModel):
    text:str

class PredictorResponse(BaseModel):
    predicted_dept:str
    confidence:float