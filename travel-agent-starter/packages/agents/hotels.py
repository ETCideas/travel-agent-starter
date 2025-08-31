from packages.core.models import TripState, BookingOrder
from packages.providers.duffel_stays import search_hotels, book_hotel

def plan(state: TripState) -> TripState:
    state.hotels = search_hotels(state.req, state.prefs)
    return state

def book(state: TripState) -> TripState:
    choice = state.approvals.get("hotel")
    if not choice:
        return state
    res = book_hotel(choice["id"], guest=choice.get("guest", {}))
    state.orders.append(BookingOrder(id=res["order_id"], component="hotel", status=res["status"], details=res))
    return state
