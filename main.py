import requests

API_KEY = "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"
API_URL = "https://api.groq.com/v1/chat/completions"

def chat_with_groq():
    print("Groq Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"prompt": user_input, "max_tokens": 100}
        )

        if response.status_code == 200:
            print("Groq:", response.json().get("choices", [{}])[0].get("text", "No response"))
        else:
            print("Error:", response.text)

if __name__ == "__main__":
    chat_with_groq()

