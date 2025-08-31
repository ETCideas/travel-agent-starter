# Stubbed Viator provider (replace with real API calls)
from packages.core.models import ExperienceOption, Price, TripRequest

def search_experiences(req: TripRequest) -> list[ExperienceOption]:
    # TODO: wire products -> availability -> bookings
    return [
        ExperienceOption(
            id="tour1",
            name="City Highlights Guided Tour",
            provider="viator",
            when=req.depart_date,
            duration_min=180,
            link="https://www.viator.com/",
            price=Price(amount=60.0, currency=req.currency, refundable=True),
        )
    ]

def book_experience(option_id: str, guest: dict) -> dict:
    return {"order_id": f"XP-{option_id}", "status": "booked"}
