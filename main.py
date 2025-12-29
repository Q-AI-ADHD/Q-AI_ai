from fastapi import FastAPI
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
from prompt.question_prompt import givemetheprompt
from prompt.feedback_prompt import givethefeedback
from llama_cpp import Llama
from pathlib import Path
app = FastAPI()

llm = Llama(
    model_path=r"C:\Users\pc\Desktop\최인규\건들면사망\q&ai\models\qwen2.5-7b-instruct-q8_0-00001-of-00003.gguf",
    n_ctx=2048,
    n_gpu_layers=0,
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ai/qna/question", response_model = questionResponse)
async def quest_create(req: questionRequest):
    prompt = givemetheprompt(req.subject,req.level,req.subjectdetail)
    out = llm(prompt, max_tokens= 256, temperature = 0.6, stop= ['\n'])
    
    quest = out['choices'][0]['text'].strip()
    print(req.subject, req.level, req.subjectdetail)
    print(quest)
    return questionResponse(question = quest)

@app.post("/ai/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    pass
    # return feedbackResponse({'feedback': pass})
