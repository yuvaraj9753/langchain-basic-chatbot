import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage

from model_session_state import get_response


# Page configuration
st.set_page_config(
    page_title="LangChain Session Memory",
    page_icon="🧠",
    layout="centered"
)


# Title
st.title("🧠 LangChain Chatbot")
st.caption("Session State Memory | LangChain + Groq")


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_input = st.chat_input("Ask me anything...")


if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)


    # Save user message in session state
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # Convert previous messages
    # into LangChain message objects
    chat_history = []

    for message in st.session_state.messages[:-1]:

        if message["role"] == "user":

            chat_history.append(
                HumanMessage(
                    content=message["content"]
                )
            )

        elif message["role"] == "assistant":

            chat_history.append(
                AIMessage(
                    content=message["content"]
                )
            )


    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(
                user_input,
                chat_history
            )

        st.markdown(response)


    # Save AI response in session state
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })