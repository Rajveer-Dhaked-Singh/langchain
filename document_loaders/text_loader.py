from langchain_community.document_loaders import TextLoader

loader = TextLoader("rajveer.txt", encoding="utf-8")
doc = loader.load()
print(type(doc))
print(len(doc))
