from fastapi import FastAPI, HTTPException
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
from prompt.question_prompt import givemetheprompt
from prompt.feedback_prompt import givethefeedback
from llama_cpp import Llama
from pathlib import Path
app = FastAPI()

llm = Llama(
    model_path="./models/qnaimodel-00001-of-00003.gguf",
    n_ctx=2048,
    n_gpu_layers=24,
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ai/qna/question", response_model = questionResponse)
async def quest_create(req: questionRequest):
    prompt = givemetheprompt(req.subject,req.level,req.subjectdetail)
    out = llm(prompt, max_tokens= 256, temperature = 0.6, stop = ['<END>'])
    
    quest = out['choices'][0]['text'].strip()
    print(req.subject, req.level, req.subjectdetail)
    print(quest)
    return questionResponse(question = quest)

@app.post("/ai/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    prompt = givethefeedback(req.question, req.answer)
    out = llm(prompt, max_tokens=756, temperature=0.4, stop=["<END>"])

    feedback = out["choices"][0]["text"].strip()
    print(req.question, req.answer)
    print(feedback)
    return feedbackResponse(feedback=feedback)