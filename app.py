# app.py

from src.chatbot import CollegeSubjectsChatbot


def main():
    bot = CollegeSubjectsChatbot()

    print("\nCollege Subjects Chatbot Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break

        intent, response = bot.get_response(question)
        print(f"\nBot ({intent}): {response}\n")


if __name__ == "__main__":
    main()