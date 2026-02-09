import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please login first")
else:
    st.title("👤 Profile")
    st.write(f"Welcome, **{st.session_state['user']}**")

    if st.button("Logout"):
        st.session_state.clear()
        st.success("Logged out")

