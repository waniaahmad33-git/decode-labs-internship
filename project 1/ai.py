responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hey! How are you?",
    "how are you": "I am fine, thank you!",
    "what is ai": "AI means Artificial Intelligence. It makes computers think like humans.",
    "what is python": "Python is a programming language. It is easy to learn.",
    "help": "You can ask me about AI, Python, or just say hello!",
    "bye": "Goodbye! Have a nice day!",
    "thanks": "You are welcome!",
}

print("Chatbot is running! Type 'exit' to stop.")
print("------------------------------------------")

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! Chatbot is closing now.")
        break

    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I did not understand that.")