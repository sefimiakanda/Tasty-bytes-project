from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Chargement du modèle au démarrage de l'API
model = joblib.load('models/best_model.joblib')

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Tasty Bytes !"}

@app.post("/predict")
def predict(data: dict):
    # Transformation du dictionnaire en DataFrame (format attendu par le modèle)
    df = pd.DataFrame([data])
    
    # Prédiction
    prediction = model.predict(df)[0]
    result = "High" if prediction == 1 else "Low"
    
    return {"recipe_category": data.get('category'), "prediction": result}