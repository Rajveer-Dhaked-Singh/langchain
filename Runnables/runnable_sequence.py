from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1= PromptTemplate(
    template="write a medium explanation on the following topic:{topic}",
    input_variables=["topic"]
)
parser= StrOutputParser()

prompt2= PromptTemplate(
    template="summarize the following explanation in one sentence: {explanation}",
    input_variables=["explanation"]
)

chain =RunnableSequence(prompt1|model|parser|prompt2|model|parser)
result=chain.invoke({"topic":"BERT"})
print(result)