# Star Type Prediction API

🔸 Welcome to the Star Type Prediction API! This project deploys a Logistic Regression model as an API using FastAPI.<br>
🔸 The model takes in various star properties as input and returns the predicted star type along with its confidence score.<br>

## Setup
Follow these steps to set up the project on your local machine:
1. **Clone the Repository:**
```
git clone https://github.com/your-username/star-type-prediction.git
cd star-type-prediction
```
2. **Create a Virtual Environment and Activate it:** 
```
conda create -name venv-name python=3.12.1
conda activate venve-name
```
3. **Install Dependencies:**
```
pip install -r requirements.txt
```

## Running the App
1. **Run the FastAPI App:**
```
uvicorn api:app --host YOUR_IP --port YOUR_PORT --reload
```
Replace `YOUR_IP` and `YOUR_PORT` with the desired IP address and port number.

2. **Access Swagger UI:**<br>
🔸 Open your web browser and navigate to `http://YOUR_IP:YOUR_PORT/docs` to access the Swagger UI.<br>
🔸 Here, you can interact with the API, input star properties, and receive predictions.

## Example of Request and Response bodies via Swagger UI

🔸 **Request body:-**
```
{
  "temperature": 2376,
  "luminosity": 0.00073,
  "radius": 0.127,
  "abs_mag": 17.22
}
```

🔸 **Response body:-**
```
{
  "predicted_probabilities": {
    "Brown Dwarf": 0.6588668588268786,
    "Hypergiant": 0.001089457863784464,
    "Main Sequence": 0.005465854764863331,
    "Red Dwarf": 0.26195464795010903,
    "Supergiant": 0.0010449570211607344,
    "White Dwarf": 0.07157822357320391
  },
  "predicted_class": "Brown Dwarf",
  "confidence": "65.9%"
}
```

## Project Structure
🔸 **api.py:** FastAPI application defining the API endpoints.<br>
🔸 **ml_star_type_prediction.ipynb:** Jupyter Notebook used for training the Logistic Regression model and saving it as model.pkl.<br>
🔸 **model.pkl:** Serialized trained model for star type prediction.<br>
🔸 **predictor.py:** Module containing functions to load the model and make predictions.<br>
🔸 **requirements.txt:** List of Python dependencies for the project.<br>
🔸 **star_properties.py:** Pydantic BaseModel and Field definitions for star properties along with set examples.<br>
🔸 **star_type_data.csv:** Dataset used for training the model.<br>

## Contribute/Queries/Suggestions
🔸 Feel free to explore and contribute to this project.<br>
🔸 If you have any questions or suggestions, please create an issue or reach out to me via rohan.calculus@gmail.com
🔸 If you find this project helpful, consider giving it a star! ⭐️ (A star for a Star Type Predictor! :D)

🌟 **Happy Star Type Prediction!** 🌌
