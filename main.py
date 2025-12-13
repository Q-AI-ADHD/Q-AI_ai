from fastapi import FastAPI
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/qna/question", response_model = questionResponse)
async def quest_create(req: questionRequest):
    return {"subject": req.subject, "level": req.level}

@app.post("/api/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    pass
    # return feedbackResponse({'feedback': pass})