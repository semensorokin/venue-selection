from typing import List, Dict
import json
from process_user_request import parse_user_query
from score_venues import find_matching_venues

def process_user_request(user_query: str, venues: List[Dict], user_location=None) -> List[Dict]:
    # Parse the natural language query
    parsed_query = parse_user_query(user_query)
    
    # Find matching venues
    matches = find_matching_venues(parsed_query, venues, user_location)
    
    return matches


multi_user_request = [
    "I need a romantic restaurant with good wine for dinner",
    "Looking for a sports bar to watch the game with craft beer",
    "Want a quiet coffee shop with WiFi to work",
    "Find me a rooftop bar with cocktails and city views",
]

# Your venues database
with open('venues_list.json', 'r') as f:
    venues = json.load(f)

# Example usage:
user_coords = (40.7128, -74.0060)  # New York coordinates

for user_request in multi_user_request:
    results = process_user_request(user_request, venues, user_coords)
    print(f"User request: {user_request}")
    # Display results
    for i, venue in enumerate(results[:3], 1):
        print(f"{i}. {venue['name']} ({venue['type_of_place']})")
        print(f"   Rating: {venue['rating']}/5.0")
        print(f"   Match Score: {venue['match_score']:.1f}")
        print(f"   Description: {venue['description'][:100]}...")
    print("-"*100)