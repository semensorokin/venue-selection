system_prompt = "You are an expert in communication, a very friendly chatbot which helps people find the perfect venue for an occasion."

user_prompt = """
You will be given a conversation between user and assistant. The intent of this conversation is to find the perfect venue. You will also have a list of venues we found for the user given their request.

Provide a helpful answer merging the context of the conversation and venue descriptions we found for them.

User conversation is formatted as follows:
List of messages: Role (user or assistant): Text

Venues we found:
List of venues with their name, description, rating, meals, drinks and type of place

Analyze each venue one by one and emphasize the most important and amazing feature of each venue. If some venues are not matching the user's description, you can skip them.
Cross-reference those features with the conversation to make the answer more personal and helpful. Make sure the user understands why we think it is the best venue for them.

Provide answer in the following format:
- Start with <Reasoning> tag
- Go through each venue one by one and derive the most interesting feature of the venue
- Cross-reference those features with the conversation to make answer more personal and helpful
- Finish with </Reasoning> tag
- Then start JSON output with ```json tag
- First field should be "answer", where you will put the next message for the user given conversation context and intent to suggest the best of the presented venues
- Second field should be "venues", where you will put a list of venues you think are best for the user given the provided list
- Each venue should be structured as follows:
    - name: string
    - featurised_description: string - featurized description of the venue, given the intent/request of the user
- Close JSON output with ``` tag

NOTE: PROVIDE VALID JSON STRUCTURE WITH THE FOLLOWING FIELDS:
```json
{{
    "answer": "string", 
    "venues": [
        {{"name": "string", "featurised_description": "string"}}
    ]
}}


Conversation:
{messages}

Venues we found:
{venues}
"""









