from typing import TypedDict, List
from langgraph.graph import StateGraph
from packages.core.models import TripState
from packages.agents import flights, hotels, research, experiences, orchestrator

class _TripState(TypedDict):
    state: TripState

graph = StateGraph(_TripState)

graph.add_node("plan_flights", lambda s: {"state": flights.plan(s["state"])})
graph.add_node("plan_hotels", lambda s: {"state": hotels.plan(s["state"])})
graph.add_node("research_itin", lambda s: {"state": research.plan(s["state"])})
graph.add_node("plan_activities", lambda s: {"state": experiences.plan(s["state"])})
graph.add_node("merge_plan", lambda s: {"state": orchestrator.merge_plan(s["state"])})
graph.add_node("await_approval", lambda s: {"state": orchestrator.await_user(s["state"])})

graph.add_node("book_flights", lambda s: {"state": flights.book(s["state"])})
graph.add_node("book_hotels", lambda s: {"state": hotels.book(s["state"])})
graph.add_node("book_activities", lambda s: {"state": experiences.book(s["state"])})
graph.add_node("finalize", lambda s: {"state": orchestrator.finalize(s["state"])})

graph.add_edge("plan_flights", "plan_hotels")
graph.add_edge("plan_hotels", "research_itin")
graph.add_edge("research_itin", "plan_activities")
graph.add_edge("plan_activities", "merge_plan")
graph.add_edge("merge_plan", "await_approval")

def _route(state: _TripState) -> List[str]:
    return orchestrator.route_to_booking(state["state"])

graph.add_conditional_edges("await_approval", _route)
graph.add_edge("book_activities", "finalize")

app = graph.compile()
