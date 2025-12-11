from pydantic import BaseModel

class questionRequest(BaseModel):
    subject: str
    level: str

class questionResponse(BaseModel):
    id: int
    question: str
    subject: str
    level: str