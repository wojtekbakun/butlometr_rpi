import csv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
def read_root():
    with open("newData.json", "r") as file:
        data = json.load(file)
        latest_data = data[-1]  # Assuming the JSON data is a list of entries
        return JSONResponse(content=latest_data)
