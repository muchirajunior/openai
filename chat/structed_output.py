from pydantic import BaseModel
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY").encode('utf-8').decode('ascii', 'ignore')

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice, mary, Sam and John are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed

print(event.name)
print(event.date)
print(event.participants)
