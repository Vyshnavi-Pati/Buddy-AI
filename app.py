import streamlit as st

st.title("🌱 BuddyAI")

st.write("A friendly space to talk, practice, and feel heard.")

message = st.chat_input("Talk to BuddyAI...")

if message:
    st.write("You said:", message)