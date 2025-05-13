import streamlit as st
from src.nlp_engine import get_ai_response

def run():
    st.title("🤖 Arogyam Chatbot")
    st.markdown("Ask me anything related to health, fitness, and general knowledge!")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input field at bottom
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message here...", key="user_input")
        submit_button = st.form_submit_button("Send")

    # If user sends a message
    if submit_button and user_input:
        # Get AI response
        bot_response = get_ai_response(user_input)

        # Save conversation
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Arogyam", bot_response))

    # Display the conversation
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(
                f"<div style='background-color: C; padding: 8px; border-radius: 8px; margin:5px; text-align:right'><b>{speaker}:</b> {message}</div>",
                unsafe_allow_html=True
            ) # import streamlit as st
from src.nlp_engine import get_ai_response

def run():
    st.title("🤖 Arogyam Chatbot")
    st.markdown("Ask me anything related to health, fitness, and general knowledge!")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input field at bottom
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message here...", key="user_input")
        submit_button = st.form_submit_button("Send")

    # If user sends a message
    if submit_button and user_input:
        # Get AI response
        bot_response = get_ai_response(user_input)

        # Save conversation
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Arogyam", bot_response))

    # Display the conversation
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(
                f"<div style='background-color: #4CAF50; padding: 8px; border-radius: 8px; margin:5px; text-align:right'><b>{speaker}:</b> {message}</div>",
                unsafe_allow_html=True
            ) # DCF8C6
        else:
            st.markdown(
                f"<div style='background-color: #333333; padding: 8px; border-radius: 8px; margin:5px; text-align:left'><b>{speaker}:</b> {message}</div>",
                unsafe_allow_html=True
            ) #F1F0F0