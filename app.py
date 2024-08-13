from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st
import ollama

def get_response(user_query, chat_history, model):

    llm = ChatOllama(model = model)

    template = """
        You are a helpful assistant.
        Answer the following questions considering the history of the conversation:
        Chat history: {chat_history}
        User question: {user_question}
        """
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query
        })

st.set_page_config(page_title="My Assistant", page_icon="🧞")
st.title("Local AI Assistant 🦾")

st.markdown('select a model from the list below')

if "model" not in st.session_state:
    st.session_state['model'] = ''

models = [model['name'] for model in ollama.list()['models']]
st.session_state['model'] = st.selectbox('Select Model', models)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hi, I'm your AI assistant. How can I help you?")]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

user_query = st.chat_input("Type your message here...")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query, st.session_state.chat_history, st.session_state.model))

    st.session_state.chat_history.append(AIMessage(content=response))



