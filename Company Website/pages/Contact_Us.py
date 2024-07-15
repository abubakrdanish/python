import pandas as pd
import streamlit as st
from send_email import send_email
st.header("Contact Me")
df=pd.read_csv("topics.csv")
with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    job_enquiry = st.selectbox("Select an Inquiry Type", df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Job Inquiry: {job_enquiry}    
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent!")