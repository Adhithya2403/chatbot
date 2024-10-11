
import streamlit as st

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you?": "I'm a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

def main():
    st.title("Simple Chatbot")
    
    user_input = st.text_input("You:")
    
    if user_input:
        bot_response = chatbot_response(user_input)
        st.text_area("Bot:", value=bot_response, height=100, max_chars=None)
    
if __name__ == "__main__":
    main()
    