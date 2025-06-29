import os
import requests
from dotenv import load_dotenv

load_dotenv("config/.env")

API_KEY = os.getenv("CEREBRAS_API_KEY")
if not API_KEY:
    raise ValueError("CEREBRAS_API_KEY environment variable not set")


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

messages = []
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        messages.append({"content": user_input, "role": "user"})

        data = {
            "model": "llama-4-scout-17b-16e-instruct",
            "stream": False,
            "messages": messages,
            "temperature": 1,
            "max_tokens": -1,
            "seed": 0,
            "top_p": 1,
        }

        # Make the POST request
        response = requests.post(
            "https://api.cerebras.ai/v1/chat/completions", headers=headers, json=data
        )

        # Check the response
        if response.status_code == 200:
            response_data = response.json()
            assistant_response = response_data["choices"][0]["message"]["content"]
            print("Cerebras: ", end="")
            print(assistant_response)

            if assistant_response:
                messages.append({"content": assistant_response, "role": "assistant"})
                # Keep only the last 10 messages to manage context length
                messages = messages[-10:]
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
