import os 
from dotenv import load_dotenv
from aiosmtplib import send
from datetime import datetime
from email.message import EmailMessage

load_dotenv()  # Load environment variables from .env file

async def send_email(summary: str, sender_email: str):
    email = EmailMessage()
    email["From"] = os.getenv("EMAIL_USER")
    email["To"] = os.getenv("EMAIL_TO")
    email["Subject"] = "🚨 Wi-Fi Issue Reported"
    email["Reply-To"] = sender_email

    email.set_content(
        f"""
Wi-Fi Issue Reported:

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Reported by: {sender_email}

Summary:
{summary}
        """.strip()
    )

    await send(
        email,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASS")
    )


