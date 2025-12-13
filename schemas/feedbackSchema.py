from pydantic import BaseModel

class feedbackRequest(BaseModel):
    qnaId: int
    question: str
    answer: str

class feedbackResponse(BaseModel):
    feedback: str