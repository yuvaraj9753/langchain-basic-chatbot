from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()


# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# Create prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. "
        "Answer clearly and simply."
    ),

    # Previous conversation
    MessagesPlaceholder(
        variable_name="chat_history"
    ),

    # Current question
    (
        "human",
        "{question}"
    )
])


# Create chain
chain = prompt | llm


def get_response(user_input, chat_history):

    response = chain.invoke({
        "question": user_input,
        "chat_history": chat_history
    })

    return response.content