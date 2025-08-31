from packages.core.models import TripState

def merge_plan(state: TripState) -> TripState:
    return state

def await_user(state: TripState) -> TripState:
    return state

def finalize(state: TripState) -> TripState:
    return state

def route_to_booking(state: TripState) -> list[str]:
    nodes = []
    if state.approvals.get("flight"): nodes.append("book_flights")
    if state.approvals.get("hotel"): nodes.append("book_hotels")
    if state.approvals.get("experiences"): nodes.append("book_activities")
    if not nodes:
        return ["finalize"]
    return nodes
