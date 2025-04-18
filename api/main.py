from fastapi import FastAPI
from api.config import initialize_api_keys

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

@app.get("/")
def root():
    return {
        "message": "🚀 Askwise API is up and running!",        
    }