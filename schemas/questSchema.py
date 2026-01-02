from pydantic import BaseModel
from typing import Optional

class questionRequest(BaseModel):
    subject: str
    level: str
    subjectdetail: str
    
class questionResponse(BaseModel):
    id: Optional[int] = None
    question: str
