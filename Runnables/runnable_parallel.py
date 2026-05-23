from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1= PromptTemplate(
    template="write a tweet about the following topic:{topic}",
    input_variables=["topic"]
)
parser= StrOutputParser()

prompt2= PromptTemplate(
    template="write a linkedin post about the following topic:{topic}",
    input_variables=["topic"]
)
chain =RunnableParallel({
    "tweet":RunnableSequence(prompt1|model|parser),
    "linkedin":RunnableSequence(prompt2|model|parser)
})
result= chain.invoke({"topic":"AI in healthcare"})
print(result["tweet"])
print(result["linkedin"])