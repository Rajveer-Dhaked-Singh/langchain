from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch

load_dotenv() 
model =ChatGroq(model="llama-3.1-8b-instant")
prompt1= PromptTemplate(
    template =" write a detailed report  on the topic: {topic}",
    input_variables=["topic"]
)
prompt2= PromptTemplate(
    template="the above report is too long, write a concise summary of it: {report}",
    input_variables=["report"]
)


parser= StrOutputParser()

def word_count(report):
    return len(report.split())

report_chain= prompt1|model|parser
branch_chain= RunnableBranch(
       (lambda x: word_count(x)>500, RunnableSequence(prompt2|model|parser)),
       RunnablePassthrough()
)    
final_chain= report_chain|branch_chain  
result= final_chain.invoke({"topic":"AI in healthcare"})
print(result) 
    