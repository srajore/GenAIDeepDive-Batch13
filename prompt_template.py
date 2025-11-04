from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate.from_template("Tell me a key achivements of {person} in 4 bulleted points in {category}?")

#from dotenv import load_dotenv

#load_dotenv()

llm = ChatOllama(model="llama3.2:latest")

chain = prompt | llm 

response = chain.invoke({"person":"Rahul Gandhi","category":"politics"})

print(response.content)


