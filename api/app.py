from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from JSON file
def load_data():
    data_path = Path(__file__).parent / "q-vercel-python.json"
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading data: {str(e)}")

# Load data at startup
@app.on_event("startup")
async def startup_event():
    app.state.data = load_data()

@app.get("/api")
async def get_marks(names: List[str] = Query(..., alias="name")):
    data = app.state.data
    marks = []
    
    for name in names:
        # Find first matching entry
        match = next((item for item in data if item["name"] == name), None)
        marks.append(match["marks"] if match else 0)
    
    return {"marks": marks}
