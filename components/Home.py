import streamlit as st
from components.ChatBot import *
# Title of the Streamlit app
def show_homepage():
    st.title("Home Page")

    # Introduction text
    st.markdown("""
    Please fill out the form below to provide your personal information. 
    Your details will help us customize your experience.
    """)

    # Create a form for collecting user input
    with st.form(key='personal_info_form'):
        st.subheader("Personal Information")

        # Input fields
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        # Submit button
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.session_state.user_data = {
            "name": name,
            "email": email,
            "age": age,
            "gender": gender,
        }
        # Change page to chatbot
        st.session_state.page = "chatbot1"


