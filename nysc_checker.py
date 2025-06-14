#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import yagmail
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

url = "https://portal.nysc.org.ng/nysc1/"
KEYWORD = "No Active Registration"

def is_registration_open():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        return KEYWORD not in soup.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return False
    
def send_email_alert():
    try:
        yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = "📢 NYSC Registration is NOW OPEN!"
        body = "Visit https://portal.nysc.org.ng/nysc1/ to register ASAP!"
        yag.send(to=RECEIVER_EMAIL, subject=subject, contents=body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_whatsapp_alert():
    try:
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="📢 NYSC Registration is NOW OPEN! Visit https://portal.nysc.org.ng/nysc1/ to register ASAP!",
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
        print("WhatsApp message sent successfully!")
    except TwilioRestException as e:
        print(f"Failed to send WhatsApp message: {e}")

def main():
    if is_registration_open():
        send_email_alert()
        send_whatsapp_alert()
    else:
        print("NYSC registration is still closed.")

if __name__ == "__main__":
    main()