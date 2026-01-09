from pydantic import BaseModel

class feedbackRequest(BaseModel):
    question: str
    answer: str

class feedbackResponse(BaseModel):
    feedback: str
