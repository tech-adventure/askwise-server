from fastapi import FastAPI, APIRouter

# Config
from api.config import initialize_api_keys

# Routers
from api.routers.interview import router as interview_router

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
async def startup_event():        
    initialize_api_keys()        


# Initialize API router
api_router = APIRouter(prefix="/api/v1", responses={404: {"description": "Not found"}})

@api_router.get("/")
async def root():
    return {"message": "🚀 Askwise API is up and running!"}

@api_router.get("/health")
async def health():
    return {"status": "ok"}

# Add the API routes to the main app
api_router.include_router(interview_router)
app.include_router(api_router)
