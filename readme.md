# Wi-Fi Support Chatbot API

A FastAPI-based chatbot designed to help users with Wi-Fi issues and generate support reports for administrators. The bot provides sarcastic and humorous responses while collecting valuable troubleshooting information.

## 🚀 Live API

**Base URL:** `https://email-agent-api-16z6.onrender.com`

## 📋 Features

- **Interactive Chat**: Sarcastic Wi-Fi support chatbot powered by Groq's Llama model
- **Session Management**: Maintains conversation history per session
- **Report Generation**: Summarizes conversations for admin review
- **Email Integration**: Sends reports via email using SMTP
- **CORS Enabled**: Ready for frontend integration

## 🛠️ Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **Groq** - LLM API for chat responses
- **Pydantic** - Data validation and serialization
- **aiosmtplib** - Async email sending
- **python-dotenv** - Environment variable management

## 📁 Project Structure

```
chat_bot/
├── main.py              # FastAPI application and endpoints
├── client.py            # Groq API integration
├── config.py            # Configuration and API key loading
├── mailer.py            # Email functionality
├── summarizer.py        # Chat summarization logic
├── requirements.txt     # Python dependencies
├── render.yaml         # Render deployment configuration
├── .env                # Environment variables (not in repo)
└── .gitignore          # Git ignore rules
```

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd chat_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
EMAIL_USER=your_smtp_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=admin@company.com
```

### 4. Run locally
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

### Base URL
```
https://email-agent-api-16z6.onrender.com
```

### Endpoints

#### 1. Chat Endpoint
**POST** `/chat`

Start or continue a conversation with the Wi-Fi support bot.

**Request Body:**
```json
{
  "session_id": "string",
  "user_message": "string"
}
```

**Response:**
```json
{
  "reply": "string",
  "session_id": "string"
}
```

**Example Request:**
```bash
curl -X POST "https://email-agent-api-16z6.onrender.com/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "",
    "user_message": "My Wi-Fi is not working"
  }'
```

**Example Response:**
```json
{
  "reply": "Oh wow, another genius who can't figure out Wi-Fi. Let me guess - have you tried the ancient art of turning it off and on again? But seriously, what exactly is 'not working'? No connection? Slow speeds? Or did your router just decide to take a vacation?",
  "session_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

#### 2. Submit Report Endpoint
**POST** `/submit-report`

Generate a summary of the conversation and optionally send it via email.

**Request Body:**
```json
{
  "session_id": "string",
  "userEmail": "user@example.com",
  "sendEmail": true
}
```

**Response:**
```json
{
  "summary": "string",
  "sent": true
}
```

**Example Request:**
```bash
curl -X POST "https://email-agent-api-16z6.onrender.com/submit-report" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "userEmail": "user@example.com",
    "sendEmail": true
  }'
```

**Example Response:**
```json
{
  "summary": "User reported Wi-Fi connectivity issues. Bot suggested basic troubleshooting steps including router restart and checking cable connections. User confirmed trying basic steps. Issue appears to be intermittent connection drops.",
  "sent": true
}
```

### Error Responses

**400 Bad Request:**
```json
{
  "detail": "Validation error message"
}
```

**404 Not Found:**
```json
{
  "detail": "No conversation found"
}
```

**500 Internal Server Error:**
```json
{
  "detail": "Error message"
}
```

## 🔄 Usage Flow

1. **Start Chat**: Send a POST request to `/chat` with an empty `session_id` to start a new conversation
2. **Continue Chat**: Use the returned `session_id` for subsequent messages in the same conversation
3. **Generate Report**: When ready, send a POST request to `/submit-report` with the `session_id` to get a summary
4. **Email Report**: Set `sendEmail: true` in the report request to email the summary to administrators

## 🚀 Deployment

The application is deployed on Render using the [`render.yaml`](render.yaml) configuration file.

### Environment Variables (Production)
Set these in your Render dashboard:
- `GROQ_API_KEY`
- `EMAIL_USER`
- `EMAIL_PASS`
- `EMAIL_TO`

## 🧪 Testing

### Interactive API Documentation
Visit the deployed API documentation:
- **Swagger UI**: `https://email-agent-api-16z6.onrender.com/docs`
- **ReDoc**: `https://email-agent-api-16z6.onrender.com/redoc`

### Sample Test Flow
```python
import requests

base_url = "https://email-agent-api-16z6.onrender.com"

# Start a conversation
chat_response = requests.post(f"{base_url}/chat", json={
    "session_id": "",
    "user_message": "My internet is slow"
})

session_id = chat_response.json()["session_id"]

# Continue conversation
requests.post(f"{base_url}/chat", json={
    "session_id": session_id,
    "user_message": "I already tried restarting the router"
})

# Generate report
report_response = requests.post(f"{base_url}/submit-report", json={
    "session_id": session_id,
    "userEmail": "user@example.com",
    "sendEmail": False
})

print(report_response.json()["summary"])
```


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions, please open an issue in the GitHub repository.