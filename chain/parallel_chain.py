from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template='Explain in detail and easy way the {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Give me crisp exam ready key points about the {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='''
Merge the below outputs and give a concise summary.

Notes:
{notes}

Key Points:
{key_points}
''',
    input_variables=['notes', 'key_points']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    notes=prompt1 | model1 | parser,
    key_points=prompt2 | model2 | parser,
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"text": "Prime Minister of India"})

print(result)
chain.get_graph().print_ascii()