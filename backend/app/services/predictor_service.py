from app.schemas.predictor import (
    PredictorRequest,
    PredictorResponse
)

def predict_department(request:PredictorRequest)->PredictorResponse:
    
    text=request.text.lower()

    if "database" in text:
        return PredictorResponse(
            predicted_dept="DB Team",
            confidence=0.92
        )
    elif "network" in text:
        return PredictorResponse(
            predicted_dept="Network Team",
            confidence=0.88
        )
    else :
        return PredictorResponse(
            predicted_dept="General Support",
            confidence=0.50
        )