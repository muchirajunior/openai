from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY").encode('utf-8').decode('ascii', 'ignore')

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    tools=[{ "type": "web_search_preview" }],
    input="What was a positive news stories from today?",
)

try: 
    for item in response.output :
        print(item,'\n')
except Exception as e:
    print(e)
