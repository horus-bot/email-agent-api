from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from client import chatbot, chatbot2
from summarizer import summarize_chat
from mailer import send_email

app = FastAPI()

# Allow all CORS for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for chat sessions
chat_sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    user_message: str

class ChatResponse(BaseModel):
    reply: str
    session_id: str

class SubmitReportRequest(BaseModel):
    session_id: str
    UserEMail: EmailStr = Field(..., alias="userEmail")
    sendEmail: bool

    class Config:
        validate_by_name = True

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    
    session_id = request.session_id
    if not session_id or session_id not in chat_sessions:
        session_id = str(uuid4())
        chat_sessions[session_id] = []

    user_message = request.user_message
    chat_sessions[session_id].append({"role": "user", "content": user_message})
    try:
        reply = chatbot(chat_sessions[session_id])
        chat_sessions[session_id].append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/submit-report")
async def submit_report(report: SubmitReportRequest):
    session_id = report.session_id
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="No conversation found")

    messages = chat_sessions[session_id]
    summary = summarize_chat(messages)

    if report.sendEmail:
        await send_email(summary, report.UserEMail)

    return {"summary": summary, "sent": report.sendEmail}
