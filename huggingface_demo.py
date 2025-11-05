from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Tell me a key achivements of Rahul Gandhi in 4 bulleted points in politics?")

print(response.content)