import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from prompts import BUDDY_SYSTEM_PROMPT


# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY is missing. Please check your .env file.")
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)


st.set_page_config(
    page_title="BuddyAI",
    page_icon="🌱"
)


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "starter" not in st.session_state:
    st.session_state.starter = None


st.title("🌱 BuddyAI")
st.caption("A safe space to talk, think, practice, and take a breath.")


# Welcome message
if not st.session_state.messages:
    st.info(
        "Hi! I'm BuddyAI. You can talk to me about your day, "
        "practice a conversation, or simply chat."
    )


# Conversation starters
if not st.session_state.messages:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Talk about my day"):
            st.session_state.starter = "I want to talk about my day."

    with col2:
        if st.button("Practice a conversation"):
            st.session_state.starter = "I want to practice a conversation."

    with col3:
        if st.button("Help me relax"):
            st.session_state.starter = (
                "I want to relax and take my mind off things."
            )


# Start a new conversation
if st.button("New Conversation"):
    st.session_state.messages = []
    st.session_state.starter = None
    st.rerun()


# Conversation mode
mode = st.selectbox(
    "What do you need right now?",
    [
        "Just talk",
        "Talk it out",
        "Sort it out",
        "Take my mind off it"
    ]
)


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Talk to BuddyAI...")


# Use a starter message if selected
if st.session_state.starter:
    user_message = st.session_state.starter
    st.session_state.starter = None


if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)


    mode_instruction = {
        "Just talk": (
            "Have a natural, relaxed conversation with the user."
        ),
        "Talk it out": (
            "Let the user express what is bothering them. "
            "Listen first and avoid immediately giving solutions."
        ),
        "Sort it out": (
            "Help the user organize what is bothering them "
            "and think through practical, realistic next steps."
        ),
        "Take my mind off it": (
            "Help the user take their mind off the situation "
            "through light conversation, humor, a simple game, "
            "or another harmless distraction."
        )
    }


    messages = [
        {
            "role": "system",
            "content": BUDDY_SYSTEM_PROMPT
        },
        {
            "role": "system",
            "content": (
                f"Current conversation mode: {mode}. "
                f"{mode_instruction[mode]}"
            )
        }
    ]

    messages.extend(st.session_state.messages)


    try:
        MODEL = "openai/gpt-oss-120b"
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        buddy_response = response.choices[0].message.content

    except Exception as e:
        buddy_response = (
            "I'm having a little trouble connecting right now. "
            "Please try again in a moment. 🌱"
        )

        st.warning(f"Temporary API issue: {e}")


    st.session_state.messages.append({
        "role": "assistant",
        "content": buddy_response
    })

    with st.chat_message("assistant"):
        st.write(buddy_response)