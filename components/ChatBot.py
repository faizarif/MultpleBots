import random
import time
from utils import *

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

def show_chatbot1():
    summary_database="chat_summary_1"
    st.title("Chatbot1")
    if "messages_1" not in st.session_state:
        database="chat_history_1"
        st.session_state.messages = load_chat_history(database)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?",key=1):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        save_chat_history(st.session_state.messages,"chat_history_1")


    if st.button("Aggregate Chats"):
        generating_summary(st.session_state.messages,10,summary_database)
        st.session_state.page = "chatbot2"
        st.session_state.messages = []
        filename="chat_history_1"
        save_chat_history([],filename)

def show_chatbot2():

    chat_summary_database="chat_summary_1"
    st.title("Chatbot2")

    if "messages_2" not in st.session_state:
        database="chat_history_2"
        st.session_state.messages = load_chat_history(database)

    summary_from_1=load_chat_summary(chat_summary_database)
    st.write(summary_from_1)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("In chat bot 2?",key=2):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        save_chat_history(st.session_state.messages,"chat_history_2")


    if st.button("Aggregate Chats"):
        generating_summary(st.session_state.messages,10,"chat_summary_2")
        st.session_state.page = "chatbot3"
        st.session_state.messages = []
        filename="chat_history_2"
        save_chat_history([],filename)


def show_chatbot3():
    chat_summary_database="chat_summary_2"
    st.title("Chatbot3")
    if "messages_3" not in st.session_state:
        database="chat_history_3"
        st.session_state.messages = load_chat_history(database)

    summary_from_2=load_chat_summary(chat_summary_database)
    st.write(summary_from_2)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?",key=3):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        save_chat_history(st.session_state.messages,"chat_history_3")

    if st.button("Aggregate Chats"):
        generating_summary(st.session_state.messages,10,"chat_summary_3")
        st.session_state.page = "lastpage"
        st.session_state.messages = []
        filename="chat_history_3"
        save_chat_history([],filename)

