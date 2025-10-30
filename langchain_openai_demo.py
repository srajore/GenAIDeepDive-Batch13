
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("Explain the theory of relativity in simple terms.")

print(response.content)

#response = client.responses.create(
#    model="gpt-4o-mini",
#    input="Explain the theory of relativity in simple terms.",
#)

