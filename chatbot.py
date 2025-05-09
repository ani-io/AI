from nltk.chat.util import Chat, reflections

# Define chatbot responses with patterns and replies
pairs = [
    [r"My name is (.*)", ["Hello %1. How are you today?", "Nice to meet you, %1!"]],
    [r"(.*)your name(.*)", ["I am a Chatbot. I don't have a particular name."]],
    [r"How are you(.*)", ["I am fine.", "I am always happy to help."]],
    [r"I am doing good(.*)", ["Nice to hear that!"]],
    [r"(Hi|Hello|Hey|hi|hello)(.*)", ["Hey there!", "Hello!"]],
    [r"(.*)created(.*)", ["I was made by a computer programmer."]],
    [
        r"(.*)(investments|money)(.*)",
        [
            "There are many options to invest money like mutual funds, regional banks, etc."
        ],
    ],
    [r"(.*)stocks(.*)", ["There are many companies to invest your money in."]],
    [
        r"(.*)(companies|money)(.*)",
        ["You can invest in companies like Amazon or Tesla."],
    ],
    [r"quit", ["Goodbye! Have a nice day."]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)


def main_menu():
    print("\n=== Chatbot Interface ===")
    print("1. Start Chat")
    print("2. Show Sample Questions")
    print("3. Exit")


def sample_questions():
    print("\n🔹 Sample Questions You Can Ask:")
    print("- My name is Alice")
    print("- What's your name?")
    print("- Hi / Hello")
    print("- How are you?")
    print("- Who created you?")
    print("- Tell me about investments")
    print("- Should I invest money in something?")
    print("- Are stocks a good option?")
    print("- Which companies should I invest money in?")
    print("- Type 'quit' to exit the chat")


def chat():
    print("\n👋 Chatbot is ready. Type your message below (type 'quit' to end chat):\n")
    chatbot.converse()


def run():
    while True:
        main_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            chat()
        elif choice == "2":
            sample_questions()
        elif choice == "3":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❗ Invalid choice. Please select a valid option.")


# Run the menu-driven chatbot
run()
