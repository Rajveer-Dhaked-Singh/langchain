from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

class Response(TypedDict):
    content: str
    metadata: dict
    
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response: Response = llm.invoke("What is the capital of France?")
print(response["content"])      