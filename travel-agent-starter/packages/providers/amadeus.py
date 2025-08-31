# Stubbed Amadeus provider (replace with real API calls)
from typing import List
from packages.core.models import TripRequest, FlightOption, Price

def search_flights(req: TripRequest) -> List[FlightOption]:
    # TODO: wire /v2/shopping/flight-offers + pricing
    return [
        FlightOption(
            id="amdx1",
            carrier="XX",
            segments=[{"from": req.origin, "to": req.destination, "depart": req.depart_date}],
            total_duration_min=180,
            bags_included=1,
            price=Price(amount=450.0, currency=req.currency),
            fare_rules="Nonrefundable; change fee applies",
        )
    ]

def book_flight(option_id: str, traveler: dict) -> dict:
    # TODO: POST booking
    return {"order_id": f"FL-{option_id}", "status": "booked"}
