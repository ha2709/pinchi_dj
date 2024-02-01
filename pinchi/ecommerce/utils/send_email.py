# utils/send_email.py

import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Function to send a verification email
def send_verification_email(email, verification_link):
    # Retrieve SMTP settings from environment variables
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")

    # Create MIME message
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = email
    message["Subject"] = "Verify Your Email Registration"

    # Email body content
    body = f"Click the following link to verify your registration: {verification_link}"
    message.attach(MIMEText(body, "plain"))

    # Sending the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
