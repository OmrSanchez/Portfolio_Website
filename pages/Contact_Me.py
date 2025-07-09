import streamlit as st
from send_email import send_email
import pandas
from pathlib import Path

csv_path = Path(__file__).parent.parent / 'topics.csv'

df = pandas.read_csv(csv_path)

st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address", placeholder="Enter email")
    topics = st.selectbox("What topic do you want to discuss?",
                          df['topic'], index=None)
    raw_message = st.text_area("Your message", placeholder="Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topics}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
       send_email(message)
       st.info("Your email was sent successfully!")
