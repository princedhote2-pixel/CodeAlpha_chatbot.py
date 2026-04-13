def greet():
    print("=" * 40)
    print("   Welcome to the Python Chatbot!")
    print("=" * 40)
    print("Type 'bye' to exit the chat.\n")


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hello there! Great to see you. How can I help you today?"

    elif user_input == "how are you":
        return "I'm doing great, thanks for asking! How about you?"

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! It was nice chatting with you. Have a wonderful day!"

    elif user_input == "what is your name":
        return "My name is PyBot! I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can chat with you! Try saying: hello, how are you, what is your name, or bye."

    elif user_input == "":
        return "You didn't type anything. Please say something!"

    else:
        return "Hmm, I don't understand that yet. Try: hello, how are you, or bye."


def start_chat():
    greet()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)
        print()

        if user_input.lower().strip() in ("bye", "goodbye"):
            break


start_chat()