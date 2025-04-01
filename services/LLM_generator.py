import os
import re
from google import genai
import app_secrets

apiKey = app_secrets.GEMINI_API_KEY
modelID = app_secrets.GEMINI_MODEL_ID

client = genai.Client(api_key=apiKey)

def generate(prompt):
    return client.models.generate_content(model="gemini-2.0-flash", contents=prompt).text





