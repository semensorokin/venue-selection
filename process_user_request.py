from typing import Dict, Optional
from data_objects import UserQuery, UserQueryAI
# from openai import OpenAI
# from dotenv import load_dotenv

# import os

# load_dotenv()

# openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_user_query(query: str) -> UserQuery:
    query_lower = query.lower()

    # Extract beverage preferences
    beverage_keywords = {
        'coffee': ['coffee', 'espresso', 'latte', 'cappuccino', 'americano'],
        'beer': ['beer', 'ale', 'lager', 'ipa'],
        'wine': ['wine', 'red wine', 'white wine', 'rosé'],
        'cocktail': ['cocktail', 'drink', 'martini', 'mojito'],
        'tea': ['tea', 'green tea', 'black tea']
    }
    
    beverage_type = None
    for bev_type, keywords in beverage_keywords.items():
        if any(keyword in query_lower for keyword in keywords):
            beverage_type = bev_type
            break
    
    # Extract location preferences
    location_preference = None
    if any(word in query_lower for word in ['near', 'nearby', 'close', 'around']):
        location_preference = 'near'
    
    # Determine venue types based on request
    venue_types = []
    if beverage_type == 'coffee':
        venue_types = ['specialty_coffee', 'restaurant', 'bar']
    elif beverage_type in ['beer', 'wine', 'cocktail']:
        venue_types = ['bar', 'club', 'restaurant']
    
    return UserQuery(
        intent="find_venue",
        beverage_type=beverage_type,
        venue_types=venue_types,
        location_preference=location_preference
    )



def extraction_of_info_from_query(query: str) -> Dict:
    system_prompt = """
    You are a helpful assistant that extracts information from a user's query.
    """

    user_prompt = """
    You need to help us to extract information to filter out best matching venue given the user's request.
    All venues are repesented by Name, Location, Type of Place, Description, Drinks, Rating, Reviews, Location.
    Step by step reasong about query  split it into parts and try to identify user intent.
    Start with identifying user intent.
    If intent is to find a venue, then you need to proceed woth the follwing steps:
    1. Reason about possible venue types that user might be interested in. Provide a list relevant venue types, but select only from the following list:
    - specialty_coffee
    - restaurant
    - bar
    ...
    - club
    - celebration_place
    2. If user described meals or drinks match it with the following list:
    - special coffee
    - bakery
    - pastry
    - salad
    - soup
    - main course
    - dessert
    - drink
    3. If user described location, then you need to identify if it is near or far from the user's location.
    Select on of the following options:
    - near
    - specific place: street, city, country, etc.
    - part of the city: midtown, downtown, etc.
    4. If rating is mention create rating range from 1.0 to 5.0. Return range {X-Y} 
    5. If user mentioned any specific venue name, then you need to return it.
    
    Output should be in the following format:
    {   
        "intent": "find_venue",
        "venue_types": ["specialty_coffee", "restaurant", "bar"],
        "meals": ["special coffee", "bakery", "pastry", "salad", "soup", "main course", "dessert", "drink"],
        "location": "near | specific place | part of the city",
        "rating": "1.0-5.0",
        "place_name": "name of the place",
        "place_location": "location of the place"
    }
    Here is the user's query: {query}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content

def parse_user_query_ai(query: str) -> Optional[UserQueryAI]:
    extraction_result = extraction_of_info_from_query(query)
    if extraction_result["intent"] == "find_venue":
        return UserQueryAI(
            intent="find_venue",
            venue_types=extraction_result["venue_types"],
            meals=extraction_result["meals"],
            location=extraction_result["location"],
            rating=extraction_result["rating"],
            place_name=extraction_result["place_name"],
            place_location=extraction_result["place_location"]
        )
    # TODO: add other intents
    return None
