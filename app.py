import streamlit as st

from model import get_response


# Page configuration
st.set_page_config(
    page_title="LangChain Chatbot",
    page_icon="🤖",
    layout="centered"
)


# Title
st.title("🤖 LangChain AI Chatbot")
st.caption("Powered by LangChain + Groq")


# Chat input
user_input = st.chat_input("Ask me anything...")


if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)


    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(user_input)

        st.markdown(response)