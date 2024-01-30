# Importing the 'pickle' module for working with serialized objects
import pickle
import numpy as np

# Function to load a pre-trained model from a pickle file
def load_model(file_path='model.pkl'):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Function to make predictions using a loaded model and input features
def make_prediction(model, features):
    probability = model.predict_proba([features]).tolist()[0]
    prediction = model.predict([features])[0]
    classes = model.classes_.tolist()
    return prediction, probability, classes