# main.py
"""FastAPI entry point for AgentShield backend.

The app includes a single router for policy evaluation. Additional routers
(e.g., audit, agents) can be added later.
"""

from fastapi import FastAPI
from app.api.routes.policy import router as policy_router

app = FastAPI(title="AgentShield", version="0.1.0")
app.include_router(policy_router, prefix="/api")

# If running directly, start uvicorn (useful for local dev)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
