from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
import shelve
load_dotenv()
from utils import *
from components.Home import show_homepage
from components.ChatBot import *
from components.last_page import *
# Define tabs for page navigation
USER_AVATAR = "👤"
BOT_AVATAR = "🤖"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    # Set up page navigation using session state
    if "page" not in st.session_state:
        st.session_state.page = "home"  # Default page

    if st.session_state.page == "home":
        show_homepage()
    elif st.session_state.page == "chatbot1":
        show_chatbot1()
    elif st.session_state.page == "chatbot2":
        show_chatbot2()
    elif st.session_state.page == "chatbot3":
        show_chatbot3()
    elif st.session_state.page == "lastpage":
        show_lastpage()

# Initialize session state for chatbot messages
if "messages" not in st.session_state:
    st.session_state.messages = []

if __name__ == "__main__":
    main()










# def page2():
#     st.title("Page 2")
#     st.write("Welcome to Page 2!")
#     if st.button("Display Chat Summary"):
#         chat_summary =load_chat_summary()
#         st.write(chat_summary)
        
#     if st.button("Go to Page 3"):
#         st.session_state.page = "Page 3"

# def page1():
#     st.title("Chatbot Interface")
#     # Load chat history from shelve file

#     with st.sidebar:
#         if st.button("Delete Chat History"):
#             st.session_state.messages = []
#             filename="chat_history"
#             save_chat_history([],filename)

#     # Display chat messages
#     for message in st.session_state.messages:
#         avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
#         with st.chat_message(message["role"], avatar=avatar):
#             st.markdown(message["content"])

#     # Main chat interface
#     if prompt := st.text_input("How can I help?"):
#         with st.chat_message("user", avatar=USER_AVATAR):
#             st.markdown(prompt)
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         response = f"Echo: {prompt}"

#         with st.chat_message("assistant", avatar=BOT_AVATAR):
#             st.markdown(response)

#         st.session_state.messages.append({"role": "assistant", "content": response})

#     # Save chat history after each interaction
#     save_chat_history(st.session_state.messages,"chat_history")
#     if st.button("Submit"):
#         st.session_state.page = "Page 2"
#         generating_summary(st.session_state.messages)


# def page3():
#     st.title("Page 3")
#     st.write("Welcome to Page 3!")
#     if st.button("Go to Page 4"):
#         st.session_state.page = "Page 4"

# if 'page' not in st.session_state:
#     st.session_state.page = "Page 1"

#  # Initialize or load chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = load_chat_history()

# # Ensure openai_model is initialized in session state
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if st.session_state.page == "Page 1":
#     page1()
# if st.session_state.page == "Page 2":
#     page2()
# if st.session_state.page=="Page 3":
#     page3()
        


