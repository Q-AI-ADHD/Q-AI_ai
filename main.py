from fastapi import FastAPI, HTTPException
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
from prompt.question_prompt import givemetheprompt
from prompt.feedback_prompt import givethefeedback
from dbs.db import engine, Base
from dbs import models
from dbs.crud import save_quests
import sqlite3
import sqlalchemy
from llama_cpp import Llama
from pathlib import Path

Base.metadata.create_all(bind = engine)
app = FastAPI()

llm = Llama(
    model_path="./models/qnaimodel-00001-of-00002.gguf",
    n_ctx=2048,
    n_gpu_layers=24,
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ai/qna/question", response_model = questionResponse)
async def quest_create(req: questionRequest):
    prompt = givemetheprompt(req.subject,req.level,req.subjectdetail)
    out = llm(prompt, max_tokens= 256, temperature = 0.6, stop= ['\n'])
    
    quest = out['choices'][0]['text'].strip()
    qnaid = save_quests(req.subject, req.level, quest)
    print(req.subject, req.level, req.subjectdetail)
    print(quest)
    return questionResponse(id = qnaid, question = quest)

from dbs.crud import get_question
@app.post("/ai/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    quest = get_question(req.qnaId)
    if not quest: raise HTTPException(status_code = 404, detail = "question not found")

    prompt = givethefeedback(req.qnaId, req.question, req.answer)
    out = llm(prompt, max_tokens = 756, temperature = 0.4, stop = ['\n'])
    feedback = out['choices'][0]['text'].strip()
    
    #디버깅
    print(req.qnaId, req.question, req.answer)
    print(feedback)
    return feedbackResponse(feedback = feedback)