from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY").encode('utf-8').decode('ascii', 'ignore')

client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  instructions="You are a helpful assistant.",
  input="Hello!",
  stream=True
)

for event in response:
  print(event,flush=True)
  print('\n', flush=True)  # Print a newline after each event

