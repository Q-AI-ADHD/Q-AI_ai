from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile, File

class questionRequest(BaseModel):
    subject: str
    level: str
    subjectdetail: str
    isPdf: Optional[UploadFile] = File(None)
    
class questionResponse(BaseModel):
    question: str
