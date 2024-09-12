import random
import time
from utils import *  # Assuming these utility functions are correctly implemented

import streamlit as st

def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hi! What's up? Don't forget to subscribe to 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need assistance? My YouTube channel 'CodingIsFun' is full of great tips: https://youtube.com/@codingisfun!",
            "Hey! Got a question? Also, subscribe to 'CodingIsFun' for awesome tutorials: https://youtube.com/@codingisfun!",
            "Hi there! How can I help? BTW, my channel 'CodingIsFun' is super cool: https://youtube.com/@codingisfun!",
            "Hello! Looking for help? Check out 'CodingIsFun' on YouTube: https://youtube.com/@codingisfun!",
            "Hey! Need assistance? 'CodingIsFun' YouTube channel has you covered: https://youtube.com/@codingisfun!",
            "Hi! Got any coding questions? Don't forget to watch 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need help? 'CodingIsFun' on YouTube is a must-see: https://youtube.com/@codingisfun!",
            "Hey there! Any questions? My channel 'CodingIsFun' rocks: https://youtube.com/@codingisfun!",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def show_chatbot_page(page_name, history_key, history_file, summary_key, summary_file):
    st.title(page_name)
    
    # Initialize session state for messages if not already present
    if history_key not in st.session_state:
        st.session_state[history_key] = load_chat_history(history_file)
    
    # Display chat messages from history
    for message in st.session_state[history_key]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state[history_key].append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state[history_key].append({"role": "assistant", "content": response})
        save_chat_history(st.session_state[history_key], history_file)
    
    # Display aggregate button and handle navigation
    if st.button("Aggregate Chats"):
        generating_summary(st.session_state[history_key], 10, summary_file)
        st.session_state[history_key] = []  # Clear messages for the next phase
        save_chat_history([], history_file)  # Clear history file

        # Move to the next page
        if page_name == "Chatbot1":
            st.session_state.page = "chatbot2"
        elif page_name == "Chatbot2":
            st.session_state.page = "chatbot3"
        elif page_name == "Chatbot3":
            st.session_state.page = "lastpage"

def main():
    # Set up page navigation using session state
    if "page" not in st.session_state:
        st.session_state.page = "chatbot1"  # Default page

    # Debug print to check current page state
    st.write(f"Current page: {st.session_state.page}")

    # Render the appropriate page based on the current state
    if st.session_state.page == "chatbot1":
        show_chatbot_page("Chatbot1", "messages_1", "chat_history_1", "chat_summary_1", "chat_summary_1")
    elif st.session_state.page == "chatbot2":
        show_chatbot_page("Chatbot2", "messages_2", "chat_history_2", "chat_summary_2", "chat_summary_2")
    elif st.session_state.page == "chatbot3":
        show_chatbot_page("Chatbot3", "messages_3", "chat_history_3", "chat_summary_3", "chat_summary_3")
    elif st.session_state.page == "lastpage":
        st.title("Last Page")
        st.write("You've reached the final page!")

if __name__ == "__main__":
    main()
