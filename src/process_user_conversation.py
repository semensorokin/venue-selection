from typing import List
import json
from anthropic import Anthropic
from src.data_objects import Venue
from src.prompts.conversation import user_prompt, system_prompt

def process_venue_related_conversation(messages: List[dict], relevant_venues: List[Venue], client: Anthropic) -> str:
    formatted_messages = messages[-5:]
    formatted_messages = [f"{message['role']}: {message['content']}" for message in formatted_messages]
    formatted_messages = "\n".join(formatted_messages)

    prompt = user_prompt.format(messages=formatted_messages, venues=relevant_venues)
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return parse_output(response.content[0].text)


def parse_output(response: str) -> dict:
    print("Row model response: ", response)
    reasoning, json_str = response.split("```json")
    json_str = json_str.replace("```", "").strip()
    data = json.loads(json_str)
    formatting_answer = data['answer']
    # formatting_answer += "\n\nVenues:\n"
    # for i, venue in enumerate(data['venues']):
    #     formatting_answer += f"####{i+1}. {venue['name']}\n{venue['featurised_description']}\n\n"
    return formatting_answer