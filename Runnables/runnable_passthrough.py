from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel

load_dotenv()

model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1= PromptTemplate(
    template="write a joke about the following topic:{topic}",
    input_variables=["topic"]
)
parser= StrOutputParser()
prompt2= PromptTemplate(
    template="write a funny response to this joke: {joke}",
    input_variables=["joke"]    
)
joke_chain = RunnableSequence(prompt1|model|parser)
chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "response": RunnableSequence(prompt2|model|parser)
    
})
final_chain= joke_chain|chain
result= final_chain.invoke({"topic":"salman khan"})
print(result["joke"])
