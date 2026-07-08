import logging
from fastapi import FastAPI
import joblib
import pandas as pd
import datetime

# Configuration du log
logging.basicConfig(filename="predictions.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

app = FastAPI()
model = joblib.load('models/best_model.joblib')

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    result = "High" if prediction == 1 else "Low"
    
    # Enregistrer la requête et le résultat
    logging.info(f"Input: {data} | Prediction: {result}")
    
    return {"recipe_category": data.get('category'), "prediction": result}