from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt template for the chatbot

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer the question as best you can."),
        ("user","Question:{question}"),
    ]
)

# streamlit frameWork

st.title("Chatbot Application")
input_question = st.text_input("Search the topic whatever you want to know about")

# OpenAI LLM
# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_question:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": input_question})
            st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

