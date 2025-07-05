from openai import OpenAI

import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY").encode('utf-8').decode('ascii', 'ignore')


client = OpenAI()

response = client.responses.create(
    model="gpt-3.5-turbo-0125",
    input=[
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "what is in this image?" },
                {
                    "type": "input_image",
                    "image_url": "https://i.pinimg.com/474x/9d/c5/eb/9dc5eb14dac3708f1f48c88912296437.jpg"
                }
            ]
        }
    ]
)

print(response.output[0].content[0].text)
