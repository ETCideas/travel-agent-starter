from packages.core.models import TripState, BookingOrder
from packages.providers.amadeus import search_flights, book_flight

def plan(state: TripState) -> TripState:
    state.flights = search_flights(state.req)
    return state

def book(state: TripState) -> TripState:
    choice = state.approvals.get("flight")
    if not choice:
        return state
    res = book_flight(choice["id"], traveler=choice.get("traveler", {}))
    state.orders.append(BookingOrder(id=res["order_id"], component="flight", status=res["status"], details=res))
    return state
