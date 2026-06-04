from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Load the trained model using joblib
try:
    model = joblib.load("model.pkl")
    print("Model 'model.pkl' loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'model.pkl' not found. Please ensure it's saved.")
    model = None # Set model to None if loading fails

@app.get("/")
async def root():
   return {"message": "AI Model API is running"}

# Define the input data structure for the model with Pydantic
class Item(BaseModel):
    features: List[float]

# Add a new endpoint for predictions with Pydantic validation and batch support
@app.post("/predict")
async def predict(items: List[Item]):
    if model is None:
        return {"error": "Model not loaded. Please ensure the model file exists and FastAPI started correctly."}, 500

    # Prepare input data for batch prediction
    input_data = np.array([item.features for item in items])

    # Make predictions using the loaded model
    predictions = model.predict(input_data).tolist()
    probabilities = model.predict_proba(input_data).tolist()

    # Combine predictions and probabilities for each item
    results = []
    for i in range(len(predictions)):
        results.append({
            "prediction": predictions[i],
            "probabilities": probabilities[i]
        })

    return results
