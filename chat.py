import os
import time
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API key from environment
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

MODEL = "models/gemini-flash-lite-latest"

print("🤖 AI Chatbot running (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=user_input
        )
        print("AI:", response.text)

    except Exception:
        print("⚠️ Rate limit hit. Waiting 30 seconds...")
        time.sleep(30)
