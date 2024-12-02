import google.generativeai as genai

import streamlit as st

genai.configure(api_key="AIzaSyBCNXbaE-3MuMkKiE_0LVWCdBco8zzJ_AQ")
model = genai.GenerativeModel('gemini-pro')

# Function to get response from AI model
def ai_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


st.title("Mama GPT- (AI-Powered Genrative Support For MOM's)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    assistant_response = ai_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
