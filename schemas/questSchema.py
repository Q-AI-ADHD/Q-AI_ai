from pydantic import BaseModel

class questionRequest(BaseModel):
    subject: str
    level: str
    subjectdetail: str
    
class questionResponse(BaseModel):
    question: str