
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-pro")

response = llm.invoke("Explain the theory of relativity in simple terms.")

print(response)

