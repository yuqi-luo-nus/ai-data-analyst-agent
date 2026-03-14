from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run_data_analyst_agent

app = FastAPI(
    title="AI Data Analyst Agent",
    description="LLM powered data analysis API",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Data Analyst Agent API running"}


@app.post("/analyze")
def analyze(req: QuestionRequest):
    result = run_data_analyst_agent(req.question)
    return result