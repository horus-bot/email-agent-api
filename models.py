from pydantic import BaseModel, EmailStr
from typing import Optional, List ,Dict

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    user_message: str

class ChatResponse(BaseModel):
    reply: str

class SubmitReportRequest(BaseModel):
    session_id: Optional[str] = None
    UserEMail: EmailStr
    sendEmail: bool = False

class SubmitReportResponse(BaseModel):
    reply: str
    summary: Optional[str] = None
    emailSent: bool 
