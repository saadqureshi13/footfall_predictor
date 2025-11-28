from fastapi import APIRouter
from datetime import date
from footfall_predictor.models.prediction import PredictionResponse
from footfall_predictor.services.predictor import FootfallPredictor

router = APIRouter()
predictor = FootfallPredictor()

@router.get("/predict", response_model=PredictionResponse)
async def get_prediction(date: date):
    return await predictor.predict(date)

    
