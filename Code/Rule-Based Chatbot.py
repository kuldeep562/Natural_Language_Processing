def chatbot_response(user_input):
    rules = {
        "hi": "Hello there!",
        "how are you": "I'm just a bot, but I'm good!",
        "what is your name": "I am a rule-based chatbot.",
        "bye": "Goodbye! Have a great day!"
    }
    user_input = user_input.lower()
    for key in rules:
        if key in user_input:
            return rules[key]
    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            print("Chatbot: Bye!")
            break
        print("Chatbot:", chatbot_response(user))
