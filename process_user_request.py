from data_objects import UserQuery


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