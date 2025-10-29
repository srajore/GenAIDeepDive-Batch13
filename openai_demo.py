
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Explain the theory of relativity in simple terms.",
)

print(response.output_text)