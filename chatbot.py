
import streamlit as st

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you?": "I'm a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "Adhithyaa": "HE IS MY MASTER",
        "Gowri shanker": "HE is the member of THE TEAM",
        "Kunal": "HE is the member of THE TEAM",
        "Ashwin ": "HE is the member of THE TEAM",
        "Team": "The team belongs to JAI SHRIRAM ENGINEERING COLLEGE TIRUPPUR",
        "How is the guide of the team": "Ms.Gokiavani HOD of cse departnment.JAI SHRIRAM ENGINEERING COLLEGE",
        "how created you": "Adhithyaa and his team",
        "how is your master ": "S Adhithyaa kumar 2nd year cse",
    }
    
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

def main():
    st.title("Team OREO")
    
    user_input = st.text_input("You:")
    
    if user_input:
        bot_response = chatbot_response(user_input)
        st.text_area("Bot:", value=bot_response, height=100, max_chars=None)
    
if __name__ == "__main__":
    main()
    
