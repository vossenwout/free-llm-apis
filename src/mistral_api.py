import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv("config/.env")

API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    raise ValueError("In config/.env MISTRAL_API_KEY is not set")

# https://docs.mistral.ai/getting-started/models/models_overview/
MISTRAL_MODEL = "mistral-medium-2505"

client = Mistral(api_key=API_KEY)

messages = []
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        messages.append({"role": "user", "content": user_input})

        chat_response = client.chat.complete(
            model=MISTRAL_MODEL,
            messages=messages,
        )

        print("Mistral: ", end="")
        full_response = chat_response.choices[0].message.content
        print(full_response)

        if full_response:
            messages.append({"role": "assistant", "content": full_response})
            messages = messages[-10:]

    except KeyboardInterrupt:
        print("\nExiting...")
        break
