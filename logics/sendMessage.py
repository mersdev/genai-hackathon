import requests
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

def sendMessage(message, target):
        message = "Hi, @"+ target + ".\n\n" + message
        response = requests.post(
            url='https://api.telegram.org/bot{0}/sendMessage'.format(os.getenv("TELEGRAM_API")),
            data={'chat_id': '-4109512193', 'text': message }).json()
        return response
