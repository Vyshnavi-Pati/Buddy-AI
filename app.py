import streamlit as st

st.title("🌱 BuddyAI")
st.write("A friendly space to talk, practice, and feel heard.")

# stores conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# get new user message
user_message = st.chat_input("Talk to BuddyAI...")

if user_message:

    # adds user's message to conversation history
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # displays user's message
    with st.chat_message("user"):
        st.write(user_message)

    # temporary response
    buddy_response = "Hey! I'm listening. Tell me what's on your mind. 🌱"

    # adds Buddy's response
    st.session_state.messages.append({
        "role": "assistant",
        "content": buddy_response
    })

    # displays Buddy's response
    with st.chat_message("assistant"):
        st.write(buddy_response)