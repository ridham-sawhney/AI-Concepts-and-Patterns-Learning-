from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="KramAi: The Sequential Intelligence", 
    version="0.0.1", 
    description="AI Framework API: Action with Reflection.",
    contact={
        "name": "Ridham Sawhney",
        "email": "sawhneyridham@gmail.com",
        "url": "https://www.ridhamsawhney.com", # Added https:// for a valid URL
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    terms_of_service="https://www.ridhamsawhney.com/terms",
    # 'public=True' is not a valid FastAPI argument, removed it.
)

@app.get("/")
def read_root():
    return {
        "name": "KramAi", 
        "version": "0.0.1", 
        "message": "Welcome to the KramAi Framework API"
    }

@app.get("/status")
def get_status(): # Renamed from read_root to get_status
    return {"status": "Orchestrator Online", "version": "0.0.1"}

@app.post("/run-task")
async def run_task(agent_name: str, task_query: str):
    # This is where your Orchestrator logic would sit
    return {"message": f"Task sent to {agent_name}", "query": task_query}

@app.post("/restart/{agent_name}")
async def restart_agent(agent_name: str, payload: dict): # Renamed function and fixed typo 'paylod'
    # This is where your Orchestrator logic would sit
    return {"message": f"Agent {agent_name} restarted", "received_payload": payload}