# Importing the BaseModel class from the Pydantic library
from pydantic import BaseModel, Field

# Defining a data model for star properties using Pydantic
class StarProperties(BaseModel):
    temperature: float = Field(..., description="Temperature of the star in Kelvin", example=2376)
    luminosity: float = Field(..., description="Luminosity of the star (wrt Sun)", example=0.00073)
    radius: float = Field(..., description="Radius of the star in solar radii (wrt Sun)", example=0.127)
    abs_mag: float = Field(..., description="Absolute magnitude of the star", example=17.22)
