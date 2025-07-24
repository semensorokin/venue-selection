import re
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

@dataclass
class UserQuery:
    intent: str  # "find_venue"
    beverage_type: Optional[str] = None
    food_type: Optional[str] = None
    venue_types: List[str] = None
    location_preference: Optional[str] = None  # "near", "downtown", etc.
    price_range: Optional[str] = None
    atmosphere: Optional[str] = None
    rating_min: Optional[float] = None

