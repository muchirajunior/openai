from openai import OpenAI
from dotenv import load_dotenv

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY").encode('utf-8').decode('ascii', 'ignore')

client = OpenAI()


response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
