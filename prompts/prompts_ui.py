from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("research tool")
user_input = st.text_input("Enter your prompt")

if st.button("Submit"):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    response = llm.invoke(user_input)
    st.write(response.content)