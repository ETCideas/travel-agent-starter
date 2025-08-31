from fastapi import FastAPI, HTTPException
from typing import Dict
from packages.core.models import TripRequest, TripState, UserPreferences
from packages.agents.trip_graph import app as trip_graph_app

app = FastAPI(title="Travel Agent API", version="0.1.0")

TRIPS: Dict[str, TripState] = {}

@app.post("/trips")
def create_trip(req: TripRequest, prefs: UserPreferences | None = None):
    state = TripState(req=req, prefs=prefs or UserPreferences())
    trip_id = f"t-{len(TRIPS)+1}"
    TRIPS[trip_id] = state
    _ = trip_graph_app.invoke({"state": state}, start_at="plan_flights", end_at="await_approval")
    return {"trip_id": trip_id}

@app.get("/trips/{trip_id}/plan")
def get_plan(trip_id: str):
    state = TRIPS.get(trip_id)
    if not state:
        raise HTTPException(404, "Trip not found")
    return state

@app.post("/trips/{trip_id}/approve")
def approve_and_book(trip_id: str, approvals: Dict):
    state = TRIPS.get(trip_id)
    if not state:
        raise HTTPException(404, "Trip not found")
    state.approvals = approvals
    _ = trip_graph_app.invoke({"state": state}, start_at="await_approval")
    return {"orders": state.orders}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    for st in TRIPS.values():
        for o in st.orders:
            if o.id == order_id:
                return o
    raise HTTPException(404, "Order not found")

@app.post("/webhooks/duffel")
def duffel_webhook(payload: Dict):
    return {"ok": True}

@app.post("/webhooks/viator")
def viator_webhook(payload: Dict):
    return {"ok": True}
