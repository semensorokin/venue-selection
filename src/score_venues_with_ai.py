from typing import List
from src.data_objects import Venue, UserIntentVenue


def score_venues(venues: List[Venue], user_intent: UserIntentVenue) -> List[Venue]:
    """
    Simple scoring function to score venues based on user intent.
    Venue types, meal types, drink types, rating, name.
    Each match increases the score by 10 points.
    Return list of venues sorted by score in descending order.
    TODO: Add more sophisticated scoring function.
    """
    for venue in venues:
        venue.score = 0
        if user_intent.venue_types and venue.type_of_place and any(venue_type in user_intent.venue_types for venue_type in venue.type_of_place):
            venue.score += 10
        if user_intent.meal_types and venue.meal_types and any(meal_type in user_intent.meal_types for meal_type in venue.meal_types):
            venue.score += 10
        if user_intent.drink_types and venue.drink_types and any(drink_type in user_intent.drink_types for drink_type in venue.drink_types):
            venue.score += 10
        if user_intent.rating and venue.rating and venue.rating >= user_intent.rating[0] and venue.rating <= user_intent.rating[1]:
            venue.score += 10
        if user_intent.name and venue.name and user_intent.name in venue.name:
            venue.score += 10
        
    return venues

def get_top_venues(venues: List[Venue], user_intent: UserIntentVenue, top_n: int = 3) -> List[Venue]:
    updated_venues = score_venues(venues, user_intent)
    venues.sort(key=lambda x: x.score, reverse=True)
    return venues[:top_n]