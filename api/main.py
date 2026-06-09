from fastapi import FastAPI
from agent.agent import analyze_email
from agent.schemas import EmailAnalysis

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Email Action Agent is running"}

@app.post("/analyze", response_model=EmailAnalysis)
def analyze(email: str):
    """
    Main endpoint:
    - receives email text
    - calls the agent
    - returns structured analysis
    """
    result = analyze_email(email)
    return result
