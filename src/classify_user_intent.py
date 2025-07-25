import json
from anthropic import Anthropic
from typing import List
from src.prompts.intent import user_prompt, system_prompt, possible_venue_types, possible_meals_types, possible_drinks_types
from src.data_objects import UserIntentVenue, UserIntentBase

def classify_user_intent(messages: List[dict], client: Anthropic) -> UserIntentBase:
    formatted_messages = messages[-5:]
    formatted_messages = [f"{message['role']}: {message['content']}" for message in formatted_messages]
    formatted_messages = "\n".join(formatted_messages)

    prompt = user_prompt.format(messages=formatted_messages, venue_types=possible_venue_types, meal_types=possible_meals_types, drink_types=possible_drinks_types)
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    response_json = parse_output(response.content[0].text)
    if response_json["intent"] == "find_venue":
        return UserIntentVenue(**response_json)
    else:
        return UserIntentBase(**response_json)


def parse_output(response: str) -> dict:
    reasoning, json_str = response.split("```json")
    json_str = json_str.replace("```", "").strip()
    print(reasoning)
    print(json_str)
    return json.loads(json_str)