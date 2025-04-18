from pydantic import BaseModel
from typing import Optional, List

class InterviewRequest(BaseModel):
    role: str
    description: str
    level: Optional[str] = None
    company: str

class InterviewResponse(BaseModel):
    questions: List[str]
