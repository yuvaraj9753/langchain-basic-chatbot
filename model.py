import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def get_response(user_input):

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful AI assistant. "
            "Answer clearly and simply."
        ),
        (
            "human",
            "{question}"
        )
    ])

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": user_input
    })

    return response.content