from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
load_dotenv(override=True)

llm = ChatBedrockConverse(
    region_name="us-east-1",
    model_id="amazon.titan-text-express-v1"
)

response = llm.invoke("What is AgenticAI?")

print(response.content)
