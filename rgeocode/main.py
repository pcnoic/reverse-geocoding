from fastapi import FastAPI
from coords import get_location
from pydantic import BaseModel
import json

class Coordinates(BaseModel):
    latitude: str
    longitude: str

app = FastAPI()
    
@app.post("/georeverse/")
async def georeverse(coords: Coordinates):
    location = get_location(coords.latitude, coords.longitude)
    location_json = json.dumps(location)
    
    return location
