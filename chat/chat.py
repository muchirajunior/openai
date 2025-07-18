from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
