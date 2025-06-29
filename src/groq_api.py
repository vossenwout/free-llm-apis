from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv("config/.env")

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("In config/.env GROQ_API_KEY is not set")

# set the GROQ model to use see:
# https://console.groq.com/docs/rate-limits#rate-limits
GROQQ_MODEL = "qwen-qwq-32b"


client = Groq(api_key=API_KEY)
messages = []
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        messages.append({"role": "user", "content": user_input})

        completion = client.chat.completions.create(
            model=GROQQ_MODEL,
            messages=messages,
            temperature=1,
            max_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )

        print("Groq: ", end="")
        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            print(content, end="")
            full_response += content
        print()

        if full_response:
            messages.append({"role": "assistant", "content": full_response})
            messages = messages[-10:]

    except KeyboardInterrupt:
        print("\nExiting...")
        break
