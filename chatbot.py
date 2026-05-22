import datetime

print("======================================")
print("      AI RULE-BASED CHATBOT 🤖")
print("======================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    # Take user input
    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "hi":
        print("Bot: Hi there!")

    elif user_input == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user_input == "good evening":
        print("Bot: Good evening!")

    elif user_input == "good night":
        print("Bot: Good night!")

    # Basic Conversation
    elif "how are you" in user_input:
        print("Bot: I am doing great. Thanks for asking!")

    elif "your name" in user_input:
        print("Bot: My name is DecodeBot.")

    elif "who made you" in user_input:
        print("Bot: I was created using Python.")

    elif "what is ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language.")

    # Time Feature
    elif "time" in user_input:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print("Bot: Current time is", current_time)

    # Date Feature
    elif "date" in user_input:

        current_date = datetime.datetime.now().strftime("%d-%m-%Y")

        print("Bot: Today's date is", current_date)

    # Joke Feature
    elif "joke" in user_input:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Motivation
    elif "motivate me" in user_input:
        print("Bot: Keep learning and never give up. Success takes time!")

    # Thank You
    elif "thank you" in user_input:
        print("Bot: You're welcome!")

    elif "thanks" in user_input:
        print("Bot: Happy to help!")

    # Help Command
    elif "help" in user_input:
        print("Bot: You can ask me about AI, Python, time, date, jokes, and more.")

    # Exit Command
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I don't understand that.")