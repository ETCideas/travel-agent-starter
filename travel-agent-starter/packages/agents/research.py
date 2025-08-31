from packages.core.models import TripState
from packages.providers.search import research_itinerary

def plan(state: TripState) -> TripState:
    state.itinerary = research_itinerary(state.req)
    return state
