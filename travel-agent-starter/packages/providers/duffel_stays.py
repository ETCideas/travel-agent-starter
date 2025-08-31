# Stubbed Duffel Stays provider (replace with real API calls)
from typing import List
from packages.core.models import HotelOption, Price, TripRequest, UserPreferences

def search_hotels(req: TripRequest, prefs: UserPreferences) -> List[HotelOption]:
    # TODO: wire search -> rates -> quote -> booking
    return [
        HotelOption(
            id="stay1",
            name="Sample Boutique Hotel",
            address="123 Main St",
            rating=4.5,
            amenities=["wifi", "gym", "breakfast"],
            refundable_until=f"{req.depart_date}T23:59:00",
            price=Price(amount=120.0, currency=req.currency, refundable=True),
        ),
        HotelOption(
            id="stay2",
            name="Downtown Plaza",
            address="45 Center Ave",
            rating=4.2,
            amenities=["wifi", "pool"],
            refundable_until=None,
            price=Price(amount=90.0, currency=req.currency, refundable=False),
        ),
    ]

def book_hotel(option_id: str, guest: dict) -> dict:
    return {"order_id": f"HT-{option_id}", "status": "booked"}
