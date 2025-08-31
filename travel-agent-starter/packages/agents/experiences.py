from packages.core.models import TripState, BookingOrder
from packages.providers.viator import search_experiences, book_experience

def plan(state: TripState) -> TripState:
    state.activities = search_experiences(state.req)
    return state

def book(state: TripState) -> TripState:
    choice = state.approvals.get("experiences")
    if not choice:
        return state
    for opt in choice.get("ids", []):
        res = book_experience(opt, guest=choice.get("guest", {}))
        state.orders.append(BookingOrder(id=res["order_id"], component="experience", status=res["status"], details=res))
    return state
