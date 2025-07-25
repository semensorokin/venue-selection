from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class UserIntentBase:
    intent: str

@dataclass
class UserIntentVenue(UserIntentBase):
    venue_types: List[str]
    meal_types: List[str]
    drink_types: List[str]
    rating: Tuple[float, float]
    name: Optional[str] = None
    is_near: bool = False

@dataclass
class Review:
    text: str
    stars_number: float

@dataclass
class Venue: 

    type_of_place: List[str]
    name: str
    description: str
    meal: List[str]
    meal_types: List[str]
    drinks: List[str]
    drink_types: List[str]
    rating: float
    reviews: List[Review]
    location: Tuple[float, float]
    