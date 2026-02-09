import streamlit as st

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username:
        st.session_state["logged_in"] = True
        st.session_state["user"] = username
        st.success("Login successful!")
    else:
        st.error("Please enter username")

