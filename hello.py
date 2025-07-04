from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
