from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY", "")
print(f"Loaded API Key: {api_key[:5]}...{api_key[-5:]}")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')
try:
    response = model.generate_content("hello")
    print("Success: ", response.text)
except Exception as e:
    print("Error: ", e)
