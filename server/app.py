from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


# Load the trained model
model = joblib.load('modelXGBoost.pkl')

app = FastAPI()

class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(request: PredictionRequest):
    features = np.array([[
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width
    ]])

    prediction = model.predict(features)
    # Return la classe prédite
    return {"prediction": int(prediction[0])}
