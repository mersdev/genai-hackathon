from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def promptToText(prompt):
    response = model.generate_content(prompt)
    return response.text