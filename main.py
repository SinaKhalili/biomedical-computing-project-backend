from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware 
import os
import random

from CoronaAnalysis import sinaFunction
from extra import get_daily_province_count

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Just keep this until it's bad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def auth_user(response: Response, code: str = None):
    """
    Analyze based on a GET
    """
    return "Use the /analyze endpoint \n Use /analyze/location/ for location"

@app.get("/analyze/location/{location}")
def auth_user(response: Response, location: str ='BC'):
    """
    Analyze based on a GET
    """
    data = get_daily_province_count()
    return {"risk": data[location]["risk"],
            "num_infected" : data[location]["num_infected"]}
