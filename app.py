# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request, jsonify
import datetime
import random

app = Flask(__name__)

def get_chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello there! How can I assist you today?",
            "Hi! DecodeBot AI at your service.",
            "Hey! What's on your mind?"
        ])
    elif "good morning" in user_input:
        return "Good morning! Hope you have a productive day ahead."
    elif "good evening" in user_input:
        return "Good evening! How can I help you unwind?"
    
    # Identity
    elif any(phrase in user_input for phrase in ["your name", "who are you"]):
        return "I am DecodeBot AI 🤖, your virtual assistant. I'm here to help!"
    
    # Well-being
    elif "how are you" in user_input:
        return random.choice([
            "I'm just a bunch of code, but I'm doing great! How about you?",
            "Operating at 100% capacity! How can I help?",
            "I'm doing fantastic. Thanks for asking!"
        ])
    
    # Tech / AI
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence. It is a field of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as learning, reasoning, and problem-solving."
    elif "python" in user_input:
        return "Python is a versatile, high-level programming language known for its readability. It's widely used in web development, data science, AI, and more!"
    
    # Fun / Utility
    elif "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it.",
            "Why did the developer go broke? Because he used up all his cache!"
        ]
        return random.choice(jokes)
    elif "motivate" in user_input:
        quotes = [
            "The secret of getting ahead is getting started. – Mark Twain",
            "It always seems impossible until it's done. – Nelson Mandela",
            "Code is poetry. Write something beautiful today."
        ]
        return random.choice(quotes)
    
    # Time / Date
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif "date" in user_input:
        now = datetime.datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}."
    
    # Utilities
    elif "help" in user_input:
        return "I can help you with: Greetings, answering 'what is AI' or 'Python', telling jokes, giving motivation, or telling the time and date. Just ask!"
    elif "thank you" in user_input or "thanks" in user_input:
        return random.choice([
            "You're very welcome!",
            "No problem at all!",
            "Glad I could help."
        ])
    
    # Goodbyes
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!"
        ])
    
    # Fallback
    else:
        return random.choice([
            "I'm sorry, I didn't quite catch that. Could you rephrase?",
            "I am still learning and don't know how to respond to that yet. Try asking for a joke or the time!",
            "Hmm, I'm not sure about that. Type 'help' to see what I can do."
        ])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response_route():
    if request.method == "POST":
        data = request.get_json()
        user_message = data.get("message", "")
    else:
        user_message = request.args.get("message", "")
        
    bot_response = get_chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
