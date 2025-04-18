from fastapi import APIRouter
from api.schemas.interview import InterviewRequest, InterviewResponse
from api.services.interview_service import InterviewService

router = APIRouter(prefix="/interview", tags=["interview"], responses={404: {"description": "Not found"}})

@router.post("/", response_model=InterviewResponse)
async def interview(request: InterviewRequest):            
    return InterviewService.run_mock_interview(request)
