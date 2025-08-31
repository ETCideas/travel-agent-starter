from packages.core.models import TripRequest, TripState, UserPreferences
from packages.agents.trip_graph import app

def test_trip_flow():
    req = TripRequest(origin="SFO", destination="NYC", depart_date="2025-10-01")
    state = TripState(req=req, prefs=UserPreferences())
    out = app.invoke({"state": state}, start_at="plan_flights", end_at="await_approval")
    s = out["state"]
    assert s.flights and s.hotels and s.itinerary.days and s.activities

    s.approvals = {"flight": {"id": s.flights[0].id}, "hotel": {"id": s.hotels[0].id}, "experiences": {"ids": [s.activities[0].id]}}
    out = app.invoke({"state": s}, start_at="await_approval")
    s2 = out["state"]
    assert len(s2.orders) == 3
