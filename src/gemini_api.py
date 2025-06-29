from google import genai
from dotenv import load_dotenv
from google.genai.types import GenerateContentConfig, ModelContent, Part, UserContent

import os

load_dotenv("config/.env")

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("In config/.env GEMINI_API_KEY is not set")

# https://ai.google.dev/gemini-api/docs/models
GEMINI_MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=API_KEY)

messages = []
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        messages.append(UserContent(parts=[Part(text=user_input)]))

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=messages,
            config=GenerateContentConfig(temperature=1),
        )

        print("Gemini: ", end="")
        full_response = response.text
        print(full_response)

        if full_response:
            messages.append(ModelContent(parts=[Part(text=full_response)]))
            messages = messages[-10:]
    except KeyboardInterrupt:
        print("\nExiting...")
        break
