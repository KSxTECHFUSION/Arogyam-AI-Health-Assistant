import streamlit as st
from src.auth import signup, login, reset_password  # Correct imports!

def login_signup_page():
    st.title("Login / Signup / Forgot Password")

    menu = ["Login", "Signup", "Forgot Password"]
    choice = st.selectbox("Select Option", menu)

    if choice == "Signup":
        st.subheader("Create New Account")
        username = st.text_input("Username", key="signup_username")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type='password', key="signup_password")

        if st.button("Signup"):
            if username and email and password:
                success, message = signup(username, email, password)
                if success:
                    st.success(message)
                    st.info("Now go to Login to login!")
                else:
                    st.error(message)
            else:
                st.warning("Please fill all fields.")

    elif choice == "Login":
        st.subheader("Login to your Account")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type='password', key="login_password")

        if st.button("Login"):
            if username and password:
                if login(username, password):
                    st.success(f"Welcome, {username}!")
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.warning("Please fill both fields.")

    elif choice == "Forgot Password":
        st.subheader("Recover Your Password")
        username = st.text_input("Username", key="forgot_username")
        email = st.text_input("Registered Email", key="forgot_email")
        new_password = st.text_input("New Password", type="password", key="forgot_new_password")

        if st.button("Recover Password"):
            if username and email and new_password:
                success, result = reset_password(username, email, new_password)
                if success:
                    st.success(result)
                    st.info("Now you can login with your new password!")
                else:
                    st.error(result)
            else:
                st.warning("Please fill all fields.")