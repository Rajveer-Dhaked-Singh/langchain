from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("my_chat_bot")
user_input = st.text_input("hi, how can I help you?")
if st.button("enter"):
    if user_input.lower() == "exit":
        st.write("Goodbye!")
    else:
        
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        response = llm.invoke(user_input)
        st.write(response.content)
  