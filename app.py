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

st.title("🌱 BuddyAI")
st.write("A friendly space to talk, practice, and feel heard.")


# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Talk to BuddyAI...")


if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)


    messages = [
        {
            "role": "system",
            "content": BUDDY_SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)


    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
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