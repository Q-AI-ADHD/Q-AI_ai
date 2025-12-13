from fastapi import FastAPI
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
from llama_cpp import Llama
app = FastAPI()

llm = Llama( 
    model_path = r"C:\Users\pc\Desktop\최인규\건들면사망\q&ai\models\qwen2.5-7b-instruct-gguf.gguf", 
    n_ctx = 4096, 
    n_gpu_layers = 0
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ai/qna/question", response_model = questionResponse)
async def quest_create(req: questionRequest):
    out = llm()
    return {"subject": req.subject, "level": req.level}

@app.post("/ai/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    pass
    # return feedbackResponse({'feedback': pass})