import os
import json
import urllib.request

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

print("--- 7AI Chatbot Ready (type 'exit' or 'quit' to stop) ---")

system_instruction = {
    "parts": [{
        "text": "Your name is 7AI. Your creator is Anish. You are a helpful student bot."
    }]
}

contents = []

while True:
    try:
        user_input = input("\nYou: ")
    except (KeyboardInterrupt, EOFError):
        break

    if user_input.lower() in ["exit", "quit"]:
        print("7AI: Goodbye!")
        break
    if not user_input.strip():
        continue

    contents.append({"role": "user", "parts": [{"text": user_input}]})

    payload = {
        "system_instruction": system_instruction,
        "contents": contents
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            bot_text = result["candidates"][0]["content"]["parts"][0]["text"]
            print(f"7AI: {bot_text}")
            contents.append({"role": "model", "parts": [{"text": bot_text}]})
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        error_body = e.read().decode("utf-8")
        print(error_body)
    except Exception as e:
        print("Error:", e)
