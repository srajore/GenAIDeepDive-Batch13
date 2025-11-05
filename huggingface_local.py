from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# pip install transformers
# pip install torch
# pip install python-certifi-win32
#from dotenv import load_dotenv

#load_dotenv(override=True)
import os

os.environ["HF_HOME"]='D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What all free resources I can use to learn AgenticAI?")

print(response.content)