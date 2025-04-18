from fastapi import FastAPI, APIRouter
from api.config import initialize_api_keys

from pydantic import BaseModel

# Schemas for the API
class InterviewRequest(BaseModel):
    role: str
    description: str
    level: str | None = None
    company: str

class InterviewResponse(BaseModel):
    questions: list[str]    



# Initialize application
app = FastAPI(
    title="Askwise API",
    description="""A FastAPI-based server for agentic AI-powered interview preparation. 
    Askwise leverages the CrewAI framework and LLM models to simulate mock interviews 
    and provide personalized coaching tailored to technical roles.""",
    version="1.0.0",
)

# Initialize API keys at startup
@app.on_event("startup")
def startup_event():        
    initialize_api_keys()        


# Initialize API router
api_router = APIRouter(prefix="/api/v1")


@api_router.get("/")
def root():
    return {"message": "🚀 Askwise API is up and running!"}

@api_router.get("/health")
def health():
    return {"status": "ok"}


# Add the API routes to the main app
app.include_router(api_router)
