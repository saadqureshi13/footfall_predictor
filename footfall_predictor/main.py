from fastapi import FastAPI
from footfall_predictor.api import predict

app = FastAPI()
app.include_router(predict.router)

@app.get("/")
def read_root():
    return {"message": "Footfall Predictor API is running!"}