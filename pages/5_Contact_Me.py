import streamlit as st

from Home import col_empty
from send_email import send_email
import pandas
from pathlib import Path
from email_validator import validate_email, EmailNotValidError

def app_validate_email(email_input):
    if email_input:
        try:
            valid_email_object = validate_email(email_input, check_deliverability=False)
            return valid_email_object.normalized
        except EmailNotValidError as e:
            st.error(f"Invalid email address: {str(e)}")
            return None
    else:
        return None

empty_col, col_title, emp_col = st.columns([0.2,0.8,0.2])

with col_title:
    st.header("Contact Me")

csv_path = Path(__file__).parent.parent / "topics.csv"
try:
    df = pandas.read_csv(csv_path)
    topics_options = df['topic'].tolist()
except FileNotFoundError:
    st.error("topics.csv not found. Please ensure it's in the correct directory.")
    topics_options = []

col_empty, col_form, col_emp = st.columns([0.2, 0.8, 0.2])
with col_form:
    with st.form(key='email_form', clear_on_submit=True, width=1000, height=600):
        user_provided_email = st.text_input("Email Address", placeholder="Enter email")
        topics_selected = st.selectbox("What topic do you want to discuss? (If other, please state down below.)", topics_options, index=None, help="Select a topic for your message.")
        raw_message_content = st.text_area("Message", placeholder="Your message here", height=300)
        submit_button = st.form_submit_button("Submit")

if submit_button:
    validated_email = app_validate_email(user_provided_email)
    if validated_email:
        if topics_selected:
            email_subject = f"New Email From: {validated_email} \nAbout: {topics_selected}"
            email_body = f"""\
From: {validated_email}
Topic: {topics_selected}
Message: {raw_message_content}
"""
            sender_password = st.secrets['PASSWORD']

            email_sent_successfully = send_email(
                subject=email_subject,
                body=email_body,
                sender_email='osanchez.python@gmail.com',
                receiver_email='osanchez.python@gmail.com',
                password=sender_password
            )
            if email_sent_successfully:
                st.success("Your email was sent successfully!")
            else:
                st.error("Failed to send email. Please try again later.")
        else:
            st.warning("Please select a topic before submitting.")
    else:
        st.warning("Please enter a valid email address.")