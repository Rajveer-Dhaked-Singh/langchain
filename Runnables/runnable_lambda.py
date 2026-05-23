from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough

load_dotenv() 
model =ChatGroq(model="llama-3.1-8b-instant")
prompt1= PromptTemplate(
    template="write a joke about the following topic:{topic}",
    input_variables=["topic"]   
)
def word_count(joke):
    return len(joke.split())

parser= StrOutputParser()
joke_chain= RunnableSequence(prompt1|model|parser)

chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})
final_chain= joke_chain|chain
result= final_chain.invoke({"topic":"salman khan"})
print(result)