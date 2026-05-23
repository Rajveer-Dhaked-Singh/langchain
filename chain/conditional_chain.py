from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal


load_dotenv()

model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description="The sentiment of the feedback, either positive or negative.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template="classify the following feedback into positive or negative: {feedback} \n {format_instructions}",
    input_variables=["feedback"], 
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template= "write a appropriate response for this positive review: {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template= "write a appropriate response for this negative review: {feedback}",
    input_variables=["feedback"]
)

parser = StrOutputParser()


classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=="positive",prompt2|model|parser),
    (lambda x: x.sentiment=="negative",prompt3|model|parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

    
chain = classifier_chain|branch_chain
result= chain.invoke({"feedback":"you are worst company i have ever seen and your product are fucking shit."})
print(result)