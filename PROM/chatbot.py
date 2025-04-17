import os
import requests

# Get API key

api_key = os.getenv("OPEN_AI_KEY")
endpoint = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

class chatbot:
    def __init__(self, message:list[dict[str, str]]):
        self.data = {
            "model": "gpt-3.5-turbo",
            "messages": message,
            "max_tokens": 1000
        }

# Start chat history with system message
role = input("What role would you like the assistant to take on?: ")

if "You are a" not in role:
    role = "You are a " + f"{role}. "

messages = [
    {"role": "system", "content": role}
]

agent = chatbot(messages)

print("🤖 assistant is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ") # required for the main loop execution and communication with the model/API

    if user_input.lower() in ["exit", "quit"]: # key condition to end the while loop
        print("👋 Bye!")
        break

    # Add user message to the conversation
    agent.data["messages"].append({"role": "user", "content": role + user_input})


    response = requests.post(endpoint, headers=headers, json=agent.data)

    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"].strip()
        messages.append({"role": "assistant", "content": bot_reply})
        print("Bot:", bot_reply)
    else:
        print("Error:", response.status_code)
        print(response.text)



