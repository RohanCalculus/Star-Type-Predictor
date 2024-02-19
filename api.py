# Libraries
from fastapi import FastAPI
from star_request_response import StarProperties, StarTypePrediction
from predictor import load_model, make_prediction
import numpy as np
from typing import Dict, Any

import warnings
warnings.filterwarnings('ignore')

# Create a FastAPI app instance
app = FastAPI()

# Load the machine learning model upon app startup
model = load_model()

# Define a route for the root URL ("/") with a simple health check response
@app.get('/')
def index_route():
    return {"health": "OK"}

# Define a route for handling POST requests to the "/predict" endpoint
# The route takes in a StarProperties object as input, which is expected to be sent in the request body
@app.post('/prediction', response_model=StarTypePrediction)
def prediction(sp: StarProperties):
    # Extract features from the StarProperties object
    features = [sp.temperature, sp.luminosity, sp.radius, sp.abs_mag]
    # Make a prediction using the loaded machine learning model
    pred_class, prob, classes = make_prediction(model, features)
    # Calculate the confidence level of the prediction
    confidence_score = f'{round(np.max(prob)*100, 1)}%'
    # Return the predicted probabilities, predicted class, and confidence in the response
    return {'predicted_probabilities': dict(zip(classes, prob)), 
            'predicted_class':pred_class,
            'confidence_score': confidence_score}

# uvicorn api:app --host 127.0.0.1 --port 8000 --reload

'''
Test on Real Star Data Taken from Wikipedia:- 
Betelgeuse (Supergiant) ~ https://en.wikipedia.org/wiki/Betelgeuse
Beta Pictoris (Main Seq) ~ https://en.wikipedia.org/wiki/Beta_Pictoris
Sirus (White Dwarf) ~ https://en.wikipedia.org/wiki/Sirius
'''
