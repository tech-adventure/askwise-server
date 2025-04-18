from fastapi import APIRouter
from api.schemas.interview import InterviewRequest, InterviewResponse

router = APIRouter(prefix="/interview", tags=["interview"], responses={404: {"description": "Not found"}})

@router.post("/", response_model=InterviewResponse)
def interview(request: InterviewRequest):
    return {"questions": ["What is your name?", "What is your favorite color?"]}