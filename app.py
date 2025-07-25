import streamlit as st
import os
from anthropic import Anthropic
from dotenv import load_dotenv
from src.classify_user_intent import classify_user_intent
from src.data_objects import Venue, UserIntentVenue
import json
from src.score_venues_with_ai import get_top_venues
from src.process_user_conversation import process_venue_related_conversation

load_dotenv()

st.title("Your Perfect Venue Finder")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

with open('data/venues_list.json', 'r') as f:
    venues = json.load(f)
    venues = [Venue(**venue) for venue in venues]


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        user_intent = classify_user_intent(st.session_state.messages, client)
        if isinstance(user_intent, UserIntentVenue):
            top_venues = get_top_venues(venues, user_intent)
            assistant_response = process_venue_related_conversation(st.session_state.messages, top_venues, client)
        else:
            response = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                messages=st.session_state.messages
            )
            
            # Get the response content
            assistant_response = response.content[0].text
            
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        # Display the response
        message_placeholder.markdown(assistant_response)
        