from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# FastAPI app
app = FastAPI(title="House Price Prediction API")

# Modelni yuklab olamiz
model = joblib.load("models/house_price_rf.joblib")
expected_cols = model.feature_names_in_

# Request modeli
class HouseFeatures(BaseModel):
    rooms: int
    area: float
    location: str
    year_built: int
    metro_distance: float

@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Ma'lumotni DataFrame ga o'tkazamiz
    new_house = pd.DataFrame([features.dict()])

    # location ni one-hot qilish
    new_house = pd.get_dummies(new_house)

    # Ustunlarni model kutayotgan tartibga keltiramiz
    for col in expected_cols:
        if col not in new_house.columns:
            new_house[col] = 0
    new_house = new_house[expected_cols]

    # Bashorat
    prediction = model.predict(new_house)[0]
    return {"predicted_price": round(float(prediction), 2)}
