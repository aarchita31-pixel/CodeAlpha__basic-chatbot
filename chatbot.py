# Simple Rule-Based Chatbot
def basic_chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to end the chat.")
    while True:
        user_input=input("You:").lower() # take input and convert to lowercase
        if user_input=="hello":
            print("Chatbot: Hii")
        elif  user_input=="how are you":
            print("Chatbot: I'm fine,thanks!")
        elif user_input=="bye":
            print("Chatbot: Goodbye!")
            break # Exit the loop and end the chat
        else:
            print("i don't understand that.")
basic_chatbot()
