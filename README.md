# Footfall Predictor

A small FastAPI service that predicts daily footfall for Nike stores in Berlin using simple heuristics and external data sources.

Key code locations
- Application entry: [footfall_predictor/main.py](footfall_predictor/main.py) (`app` FastAPI instance).
- API route: [footfall_predictor/api/predict.py](footfall_predictor/api/predict.py) -> [`get_prediction`](footfall_predictor/api/predict.py).
- Prediction model: [footfall_predictor/models/prediction.py](footfall_predictor/models/prediction.py) -> [`PredictionResponse`](footfall_predictor/models/prediction.py), [`WeatherInfo`](footfall_predictor/models/prediction.py).
- Services:
  - Weather: [footfall_predictor/services/weather_service.py](footfall_predictor/services/weather_service.py) -> [`WeatherService`](footfall_predictor/services/weather_service.py).
  - Holidays: [footfall_predictor/services/holiday_service.py](footfall_predictor/services/holiday_service.py) -> [`HolidayService`](footfall_predictor/services/holiday_service.py).
  - Predictor orchestration: [footfall_predictor/services/predictor.py](footfall_predictor/services/predictor.py) -> [`FootfallPredictor`](footfall_predictor/services/predictor.py).
- Config: [footfall_predictor/config.py](footfall_predictor/config.py)
- Tests: [tests/test_predict.py](tests/test_predict.py)

Requirements
- Python 3.10+
- Dependencies are declared in [pyproject.toml](pyproject.toml).

Installation

```sh
# Create virtual environment and install
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install poetry
poetry install

# run the FastAPI app with uvicorn
uvicorn footfall_predictor.main:app --reload
```

### API

GET /predict
-    Implemented in footfall_predictor/api/predict.py as get_prediction.
-    Query parameter: date (ISO date, e.g. 2025-01-01)
-    Response model: PredictionResponse

### Example request

```sh
curl "http://127.0.0.1:8000/predict?date=2025-01-01"
```
### Behavior notes

- Weather data is fetched by WeatherService from the Open-Meteo API.
- Holidays are checked by HolidayService using the Nager.Date public holidays API.
- The prediction logic lives in FootfallPredictor and currently uses simple heuristics (placeholder for an ML model).

### Testing

- See tests/test_predict.py.

### Contributing

- Follow standard Python project practices.
- Add or replace the heuristic in FootfallPredictor with a trained model in footfall_predictor/ml/model.py.


