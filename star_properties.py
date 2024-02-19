# Importing the BaseModel class from the Pydantic library
from pydantic import BaseModel, Field

# Defining a data model for star properties using Pydantic
class StarProperties(BaseModel):
    temperature: float = Field(description="Temperature of the star in Kelvin", example=2376)
    luminosity: float = Field(description="Luminosity of the star (wrt Sun)", example=0.00073)
    radius: float = Field(description="Radius of the star in solar radii (wrt Sun)", example=0.127)
    abs_mag: float = Field(description="Absolute magnitude of the star", example=17.22)

pred_prob_example = {
    "Brown Dwarf": 0.6588668588268786,
    "Hypergiant": 0.001089457863784464,
    "Main Sequence": 0.005465854764863331,
    "Red Dwarf": 0.26195464795010903,
    "Supergiant": 0.0010449570211607344,
    "White Dwarf": 0.07157822357320391
  }

class StarTypePrediction(BaseModel):
    predicted_probabilities: dict = Field(description="Predicted probabilities for all classes.", example=pred_prob_example)
    predicted_class: str = Field(description="Predicted class based on the highest probability.", example='Brown Dwarf')
    confidence_score: str = Field(description="Confidence score indicating the model's certainty in the predicted class.", example="65.9%")