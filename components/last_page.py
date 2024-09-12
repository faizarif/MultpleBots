import streamlit as st
from utils import *

def show_lastpage():

    # Text content
    text_content = "This is a sample text file that can be downloaded."
    chat_summary_database="chat_summary_3"


    summary_from_3=load_chat_summary(chat_summary_database)
    st.write(summary_from_3)
    # Create download button for text file
    st.download_button(
        label="Download File",
        data=text_content,
        file_name="sample.txt",
        mime="text/plain",
    )