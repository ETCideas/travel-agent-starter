# Web search stub (replace with Tavily/SerpAPI integration)
from packages.core.models import Itinerary, ItineraryDay, TripRequest

TRUSTED_SITES = ["https://www.visitacity.com", "https://www.timeout.com", "https://www.lonelyplanet.com"]

def research_itinerary(req: TripRequest) -> Itinerary:
    # TODO: call Tavily/SerpAPI and extract/cluster into days
    return Itinerary(days=[
        ItineraryDay(date=req.depart_date, items=[
            {"title": "Old Town Walk", "source": TRUSTED_SITES[1], "notes": "Morning stroll"},
            {"title": "Museum A", "source": TRUSTED_SITES[2], "notes": "Buy tickets ahead"},
        ])
    ])
