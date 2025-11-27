import streamlit as st
import random
import time

# --- BACKEND LOGIC ---
def get_bot_response(user_input):
    """
    Simple rule-based logic to determine the bot's response.
    In a real app, this would connect to an AI model or database.
    """
    user_input = user_input.lower()

    # predefined responses
    responses = {
        "hello": ["Hi there!", "Hello! How can I help?", "Greetings!"],
        "how are you": ["I'm just a bot, but I'm doing great!", "Functioning within normal parameters."],
        "python": ["Python is awesome! It's great for data science and web apps.", "I love Python too!"],
        "bye": ["Goodbye! Have a nice day.", "See you later!"]
    }

    # Search for keywords in user input
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Default fallback response
    return "I'm not sure how to respond to that. Try asking about 'Python' or say 'Hello'."

# --- FRONTEND UI (Streamlit) ---

# 1. Page Configuration
st.set_page_config(page_title="My Python Chatbot", page_icon="🤖")
st.title("🤖 Simple Python Chatbot")
st.markdown("This is a simple bot built entirely in Python using Streamlit.")

# 2. Initialize Chat History (State Management)
# Streamlit reruns the script on every interaction, so we need to save history in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Chat History
# Loop through the history and display messages on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle User Input
if prompt := st.chat_input("What is on your mind?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate Bot Response
    response = get_bot_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Simulate typing speed for realism
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})