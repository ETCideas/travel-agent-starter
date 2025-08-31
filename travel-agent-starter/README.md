# Travel Agent (Minimal LangGraph + FastAPI scaffold)

A minimal, GitHub-ready scaffold for a multi-agent travel planning + booking app with **five cooperating agents**:
1. Flights agent
2. Hotels agent
3. Itinerary research agent (web search)
4. Experiences agent (Viator/TripAdvisor/etc)
5. Orchestrator agent (glue)

> This starter repo ships with stubbed providers and agents. Wire real APIs (Amadeus/Duffel/Viator/Tavily/SerpAPI) next.

## Stack
- Python 3.11+
- FastAPI (HTTP API)
- LangGraph (agent orchestration)
- Pydantic (schemas)
- Uvicorn (dev server)
- pytest (tests)

## Layout
```
travel-agent/
  apps/api/                # FastAPI app
  packages/core/           # Pydantic models & shared types
  packages/providers/      # Thin SDK wrappers (stubs) for Amadeus/Duffel/Viator/Search
  packages/agents/         # 5 agents + LangGraph graph
  infra/docker/            # Dockerfile(s)
  tests/                   # smoke tests
  .github/workflows/       # CI
  requirements.txt
```

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn apps.api.main:app --reload
# open http://127.0.0.1:8000/docs
```

## Endpoints
- `POST /trips` — start orchestration (returns `trip_id`)
- `GET  /trips/{trip_id}/plan` — merged plan
- `POST /trips/{trip_id}/approve` — approve components to book (stub booking)
- `GET  /orders/{order_id}` — booking order lookup (stub)
- `POST /webhooks/duffel` — webhook stub
- `POST /webhooks/viator` — webhook stub
