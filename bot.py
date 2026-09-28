import re
import random
def detect_intent(user_input):
    clean_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if re.search(r'\b' + re.escape(pattern) + r'\b', clean_input):
                return intent
    return "unknownn"

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "whatsup", "whats up", "greetings"],
        "responses": ["Hey there!", "Hello! How's it going?", "What's up!", "Hi! Good to chat with you."]
    },
    "status": {
        "patterns": ["how are you", "how are u", "hows it going", "how you doing"],
        "responses": ["I'm doing great!", "Running smooth right inside Termux!", "All systems operational!"]
    },
    "identity": {
        "patterns": ["who are you", "what is your name", "what are you","who made you"],
        "responses": ["I'm a bot","you can call me 7ai", "I'm an ai bot chat.","im made in termux by Anish,the founder of s7"]
    }
}

def detect_intent(user_input):
    clean_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in clean_input:
                return intent
    return "unknown"

print("--- Dynamic Intent Chatbot Initialized ---")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    intent = detect_intent(user_input)
 
    if intent != "unknown":
        reply = random.choice(intents[intent]["responses"])
    else:
        reply = "I don't understand that intent yet. Try asking differently!"

    print(f"Bot: {reply}\n")
