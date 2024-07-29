import africastalking
import dotenv
import os
from typing import Dict

dotenv.load_dotenv()

username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')
africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_sms(message: Dict[str, str]) -> None:
    """
    Function that sends an SMS to a specified number.
    """
    try:
        sms_message = message['sms_message']
        phone_no = message['phone_no']
        response = sms.send(sms_message, [phone_no])
        return response
    except Exception as e:
        return f"Error while sending message: {e}"