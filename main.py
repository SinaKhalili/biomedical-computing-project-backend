from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware 
import os
import random

from CoronaAnalysis import sinaFunction

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
    return "Use the /analyze endpoint"

@app.post("/analyze")
def auth_user(response: Response, code: str = None):
    """
    Analyze a user POST request
    """
    return {"risk": random.randint(0,100)}

@app.get("/analyze/{location}")
def auth_user(response: Response, location: str ='BC'):
    """
    Analyze based on a GET
    """
    risk = sinaFunction(location)
    return {"risk": risk}
