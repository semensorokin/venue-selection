possible_venue_types = [
    'poker_room', 'farmers_market', 'food_truck', 'pool_hall', 'bar', 'bakery', 'cigar_lounge', 'bingo_hall', 
    'cider_house', 'casino', 'sports_bar', 'wine_bar', 'celebration_place', 'arcade_bar', 'drive_in_theater', 
    'dive_bar', 'nightclub', 'meadery', 'strip_club', 'specialty_coffee', 'speakeasy', 'hookah_lounge', 'juice_bar', 
    'food_truck_park', 'barbecue_restaurant', 'club', 'bookstore', 'escape_room', 'ice_cream_parlor', 'comedy_club', 
    'restaurant', 'axe_throwing', 'rooftop_bar', 'cocktail_bar', 'brewery', 'diner', 'record_store', 'karaoke_bar', 
    'board_game_cafe', 'art_gallery', 'mini_golf', 'gastropub', 'beach_bar', 'distillery', 'bowling_alley', 'tea_house', 
    'food_hall', 'cat_cafe'
]

possible_meals_types = [
    'appetizer', 'main course', 'dessert'
]

possible_drinks_types = [
    'wine', 'beer', 'cognac', 'other', 'juice', 'cocktail', 'rum', 'tea', 'champagne', 'coffee', 'whiskey'
]

system_prompt = """
You are a helpful assistant that classifies and extracts information from conversations.
"""

user_prompt = """
You will be given a conversation between a user and an assistant (can be a single user message if the conversation just started).

Analyze the last user message step by step and classify user intent given the last user message. 
There are only two options: ["find_venue", "other"]. 

If intent is "other", return JSON with the following structure. Always start with ```json and end with ```.
```json
{{
    "intent": "other"
}}

If intent is "find_venue", then you need to extract information to filter out the best matching venue given the user's request.
To do that, try to identify the following from user messages. Analyze all messages step by step and infer the following information:

Venue types - think about user intention and select the most appropriate place: {venue_types}
Meal types - think about user intention and select the most appropriate meals: {meal_types}
Drink types - think about user intention and select the most appropriate drinks: {drink_types}
Rating - if user mentioned rating, then you need to return rating range from 1.0 to 5.0. Return range [X, Y]; if not, return [4.5, 5.0]
Name - if user mentioned a specific venue name, then you need to return it; if not, return null
is_near - if user mentioned "near" or "nearby", then you need to return true; if not, return false

Return JSON with the following structure. Always start with ```json and end with ```.
```json
{{
    "intent": "find_venue",
    "venue_types": ["venue_type1", "venue_type2"],
    "meal_types": ["meal_type1", "meal_type2"],
    "drink_types": ["drink_type1", "drink_type2"],
    "rating": [X, Y],
    "name": "venue_name",
    "is_near": true
}}
```
EXPECTED OUTPUT:

Start with <Reasoning> tag
Think step by step and provide reasoning for your answer
Finish with </Reasoning> tag
Start JSON object with ```json tag
Close JSON object with ``` tag

Here are messages for analyzing: {messages}
"""