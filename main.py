from fastapi import FastAPI
from schemas.feedbackSchema import feedbackRequest, feedbackResponse
from schemas.questSchema import questionRequest, questionResponse
from utils.prompt import givemetheprompt
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
    out = llm(f"""
        당신은 15년차 개발자 출신의 기술 면접관입니다.
        아래 질문 사항에 맞추어 질문을 한가지 해주세요
        질문 난이도 {req.level} || 스택 {req.subject} || 세부분야 {req.subjectdetail}
        질문 사항 :
        - 면접자에 대한 기술 스택에 대하여 냉정하고 현실적으로 질문을 합니다.
        - 면접자의 스택에 대한 질문을 합니다.
        - 면접자의 질문 난이도에 맞는 질문을 합니다.
        - 반드시 질문을 할 때에는 어떠한 포맷팅을 사용하지 않습니다.
        - 반드시 존댓말을 사용하여 질문을 합니다.
        - 질문을 할때 어떠한 이모지도 사용하지 않습니다.
        - 반드시 한국어로 질문을 합니다

        어떠한 다른 예시 및 표현 없이 질문만 출력해주세요.

        코드를 출력하는 것이 아닌 한 질문만 생성해주세요.
        """, max_tokens= 256, temperature = 0.6, stop= ['\n'])
    
    quest = out['choices'][0]['text'].strip()
    print(req.subject, req.level, req.subjectdetail)
    print(quest)
    return questionResponse(question = quest)

@app.post("/ai/qna/feedback", response_model=feedbackResponse)
async def quest_feedback(req: feedbackRequest):
    pass
    # return feedbackResponse({'feedback': pass})