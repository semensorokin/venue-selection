import math
import re
from typing import List, Dict
from data_objects import UserQuery

def find_matching_venues(query: UserQuery, venues: List[Dict], user_location=None) -> List[Dict]:
    matches = []
    
    for venue in venues:
        score = calculate_venue_score(venue, query, user_location)
        if score > 0:
            venue_with_score = venue.copy()
            venue_with_score['match_score'] = score
            matches.append(venue_with_score)
    
    # Sort by match score descending
    matches.sort(key=lambda x: x['match_score'], reverse=True)
    return matches[:10]  # Return top 10 matches

def calculate_venue_score(venue: Dict, query: UserQuery, user_location=None) -> float:
    score = 0.0
    
    # 1. Venue type matching (high weight)
    if query.venue_types and venue['type_of_place'] in query.venue_types:
        score += 30
    
    # 2. Beverage availability (high weight)
    if query.beverage_type and venue.get('drinks'):
        beverage_found = check_beverage_availability(venue['drinks'], query.beverage_type)
        if beverage_found:
            score += 25
    
    # 3. Location proximity (if user location provided)
    if user_location and query.location_preference == 'near':
        distance_score = calculate_distance_score(venue['location'], user_location)
        score += distance_score
    
    # 4. Rating bonus
    if venue.get('rating'):
        score += venue['rating'] * 5  # Max 25 points for 5-star rating
    
    # 5. Description and review analysis
    text_score = analyze_text_relevance(venue, query)
    score += text_score
    
    return score

def check_beverage_availability(drinks: List[str], beverage_type: str) -> bool:
    drinks_text = ' '.join(drinks).lower()
    
    beverage_patterns = {
        'coffee': r'coffee|espresso|latte|cappuccino|americano|mocha',
        'beer': r'beer|ale|lager|ipa|stout|pilsner',
        'wine': r'wine|red wine|white wine|rosé|champagne',
        'cocktail': r'cocktail|martini|mojito|whiskey|vodka|gin',
        'tea': r'tea|green tea|black tea|herbal tea'
    }
    
    pattern = beverage_patterns.get(beverage_type, beverage_type)
    return bool(re.search(pattern, drinks_text))

def analyze_text_relevance(venue: Dict, query: UserQuery) -> float:
    score = 0.0
    search_terms = []
    
    if query.beverage_type:
        search_terms.append(query.beverage_type)
    
    # Combine description and reviews text
    text_content = venue.get('description', '').lower()
    for review in venue.get('reviews', []):
        text_content += ' ' + review.get('text', '').lower()
    
    for term in search_terms:
        if term in text_content:
            score += 5
    
    return score



def calculate_distance_score(venue_location: tuple, user_location: tuple, max_distance_km: float = 10) -> float:
    """Calculate distance-based score (closer venues get higher scores)"""
    distance = haversine_distance(venue_location, user_location)
    
    if distance > max_distance_km:
        return 0
    
    # Linear decay: closer venues get higher scores
    score = (max_distance_km - distance) / max_distance_km * 20
    return max(0, score)

def haversine_distance(coord1: tuple, coord2: tuple) -> float:
    """Calculate distance between two coordinates in kilometers"""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    R = 6371  # Earth's radius in kilometers
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat/2)**2 + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
         math.sin(dlon/2)**2)
    
    c = 2 * math.asin(math.sqrt(a))
    return R * c