from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
Generate a JSON object with the following keys for the topic '{topic}':
- summary: short summary
- key_points: list of 3 key points
- difficulty: "easy", "medium", or "hard"

JSON:
"""
)
parser = JsonOutputParser()
chain =prompt|model|parser
result= chain.invoke({"topic": "quantum computing"})
print(result)

