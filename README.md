# Venue Selection

A Python tool for matching user requests to the best venues (restaurants, bars, cafes, etc.) based on natural language queries, preferences, and location. The system parses user intent and scores venues from a database to recommend the most relevant options.

## Features
- Parses natural language user requests (e.g., "I need a romantic restaurant with good wine for dinner")
- Matches and scores venues based on type, drinks, rating, proximity, and text relevance
- Supports location-based recommendations
- Easily extensible for new venue types or preferences

## Project Structure
- `main.py`: Main entry point; processes user requests and prints top venue matches
- `process_user_request.py`: Parses user queries into structured data
- `score_venues.py`: Scores and ranks venues based on query and venue attributes
- `data_objects.py`: Data classes for structured query representation
- `venues_list.json`: Example database of venues (restaurants, bars, etc.)

## Setup
1. **Clone the repository**
2. **Install Python 3.7+**
3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies** (all are standard library, no external packages required)

## Usage
1. Place your venues database in `venues_list.json` (see format below)
2. Run the main script:
   ```bash
   python main.py
   ```
3. The script will process several example user requests and print the top venue matches for each.

### Expected Output 
```
User request: I want to go to a farmers market to buy some fresh produce
1. Le Bernardin Moderne (['restaurant'])
   Rating: 4.9/5.0
   Match Score: 24.5
   Description: Michelin-starred French restaurant specializing in exquisite seafood preparations. Features a tastin...
2. Garden Pavilion Events (['celebration_place'])
   Rating: 4.8/5.0
   Match Score: 24.0
   Description: Elegant outdoor wedding and event venue surrounded by manicured gardens and a charming gazebo. Perfe...
3. The Hidden Library (['speakeasy'])
   Rating: 4.8/5.0
   Match Score: 24.0
   Description: Secret speakeasy hidden behind a bookshelf in an antique bookstore. Prohibition-era cocktails served...
```

## Example Output
```
User request: I need a romantic restaurant with good wine for dinner
1. Mama Rosa's Trattoria (restaurant)
   Rating: 4.5/5.0
   Match Score: 60.0
   Description: Family-owned Italian restaurant serving authentic recipes passed down through generations. Cozy atmosph...
...
```

## Venue Database Format (`venues_list.json`)
Each venue is a JSON object with fields like:
```json
{
  "type_of_place": ["restaurant"],
  "name": "Mama Rosa's Trattoria",
  "description": "Family-owned Italian restaurant...",
  "meal": ["Spaghetti Carbonara - $18", ...],
  "drinks": ["Chianti Classico - $9", ...],
  "rating": 4.5,
  "reviews": [
    {"text": "Best Italian food outside of Italy!", "stars_number": 5.0},
    ...
  ],
  "location": [41.8781, -87.6298]
}
```
- `type_of_place`: List of venue types (e.g., restaurant, bar, coffee shop)
- `name`: Venue name
- `description`: Text description
- `meal`: List of food items
- `drinks`: List of drink items
- `rating`: Float (0-5)
- `reviews`: List of review objects
- `location`: [latitude, longitude]

## Customization
- Add new venues to `venues_list.json`
- Extend query parsing in `process_user_request.py` for more preferences (e.g., food type, atmosphere)
- Adjust scoring logic in `score_venues.py` for different weights or new criteria

## License
MIT License
