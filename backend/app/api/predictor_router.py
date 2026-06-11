from fastapi import APIRouter
from app.schemas.predictor import (
    PredictorRequest,
    PredictorResponse
)
from app.services.predictor_service import predict_department

router=APIRouter(
    prefix="/predict",
    tags=["prediction"]
)
@router.post(
    "/",
    response_model=PredictorResponse
)
def predict(
        request:PredictorRequest
):
    return predict_department(request)