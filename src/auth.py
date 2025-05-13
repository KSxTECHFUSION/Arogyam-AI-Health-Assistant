import streamlit as st
import json
import os
import hashlib

USER_FILE = "users.json"  # File to store user data

# Load users from JSON
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to JSON
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sign up new user
def signup(username, email, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    for user in users.values():
        if user["email"] == email:  # Check if email is already registered
            return False, "Email already registered."
    users[username] = {
        "email": email,
        "password": hash_password(password)
    }
    save_users(users)
    return True, "User registered successfully."

# Login existing user
def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == hash_password(password):
        return True
    return False

# Reset password if email matches
def reset_password(username, email, new_password):
    users = load_users()
    if username in users and users[username]["email"] == email:
        users[username]["password"] = hash_password(new_password)
        save_users(users)
        return True, "Password reset successfully."
    return False, "Username and Email do not match."

# Initialize session state
def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None