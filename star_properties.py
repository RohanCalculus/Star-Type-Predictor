# Importing the BaseModel class from the Pydantic library
from pydantic import BaseModel

# Defining a data model for star properties using Pydantic
class StarProperties(BaseModel):
    temperature: int
    luminosity: float
    radius: float
    abs_mag: float
