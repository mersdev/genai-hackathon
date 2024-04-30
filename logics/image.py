from dotenv import load_dotenv
import google.generativeai as genai
import os
import PIL.Image

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

def imageToText(prompt, image):
    
    img = PIL.Image.open('./'+image)
    response = model.generate_content([prompt,img],stream=True)
    response.resolve()
    return response.text