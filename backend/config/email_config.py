email_config.py

from typing import Dict
from email.message import EmailMessage
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL = "rohinipandhare12@gmail.com"
PASSWORD = "qjxy wqdm xriw ovnt"


def send_anomaly_email(to_email: str, anomaly: Dict):
    subject = "🚨 Log Anomaly Detected"

    body = f"""
🚨 Anomaly Detected in System Logs

Time Window : {anomaly['timestamp']}
Error Count : {anomaly['error_count']}
Z-Score     : {round(anomaly['z_score'], 2)}

Please investigate immediately.

Regards,
Log Monitoring System
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)