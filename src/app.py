import streamlit as st
import sys
import os
from streamlit_option_menu import option_menu  # New import

# Add the src directory to the Python path to ensure modules are found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import authentication functions and Streamlit apps
import auth  # Import authentication functions from auth.py
from streamlit_apps import app_diabetes, app_heart, app_chatbot
from streamlit_apps.app_login import login_signup_page  # Import the login/signup page

# Set page config
st.set_page_config(page_title="Arogyam", page_icon="❤", layout="centered")

# Sidebar function
def sidebar():
    with st.sidebar:
        st.image("https://cdn-icons-gif.flaticon.com/13099/13099799.gif", width=100)  # Logo (optional)
        st.title("Arogyam Dashboard")
        selected = option_menu(
            menu_title="Select a Service",
            options=["Diabetes Prediction", "Heart Disease Prediction", "Arogyam Chatbot", "Logout"],
            icons=["activity", "heart-pulse", "robot", "box-arrow-left"],  # Icons
            menu_icon="cast",  # Icon beside "Select a Service"
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#0E1117"},
                "icon": {"color": "white", "font-size": "18px"},
                "nav-link": {"color": "white", "font-size": "18px", "text-align": "left"},
                "nav-link-selected": {"background-color": "#FF4B4B"},
            }
        )
        return selected

# Main function for app logic
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # If not logged in, show login/signup page
    if not st.session_state['logged_in']:
        login_signup_page()
        return  # Stop further execution until user logs in

    # If logged in, show the dashboard
    selected_service = sidebar()

    if selected_service == "Diabetes Prediction":
        app_diabetes.run()
    elif selected_service == "Heart Disease Prediction":
        app_heart.run()
  #  elif selected_service == "Parkinson's Diseases Prediction":
   #     app_parkinsons.run()
    elif selected_service == "Arogyam Chatbot":
        app_chatbot.run()
    elif selected_service == "Logout":
        st.session_state['logged_in'] = False
        st.rerun()

if __name__ == "__main__":
    main()