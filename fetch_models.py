import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("No API key found in .env")
    exit(1)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
if response.status_code == 200:
    models = response.json()
    print("Available models:")
    for model in models.get("data", []):
        print(f"- {model.get('id')}")
else:
    print(f"Error fetching models: {response.status_code} - {response.text}")
