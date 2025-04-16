import os
import requests

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
endpoint = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Start chat history with system message
messages = [
    {"role": "system", "content": "You are a friendly and funny assistant."}
]

print("🤖 Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    # Add user message to the conversation
    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 100
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"].strip()
        messages.append({"role": "assistant", "content": bot_reply})
        print("Bot:", bot_reply)
    else:
        print("Error:", response.status_code)
        print(response.text)
