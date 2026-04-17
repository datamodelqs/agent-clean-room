from fastapi import FastAPI
from cleanroom.core.registry import load_workflows, get_workflow
from cleanroom.models.workflow import WorkflowStartRequest

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Agent Clean Room API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/workflows")
def workflows():
    return {"workflows": load_workflows()}


@app.post("/v1/workflows/start")
def start_workflow(request: WorkflowStartRequest):
    workflow = get_workflow(request.workflow_id)

    if not workflow:
        return {
            "status": "denied",
            "reason": "unknown workflow",
            "workflow_id": request.workflow_id,
        }

    if not workflow.get("enabled", False):
        return {
            "status": "denied",
            "reason": "workflow disabled",
            "workflow_id": request.workflow_id,
        }

    return {
        "status": "accepted",
        "workflow_id": request.workflow_id,
        "workflow": workflow,
    }