from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, HTTPException

from cleanroom.core.registry import get_workflow, load_workflows
from cleanroom.models.workflow import WorkflowStartRequest

app = FastAPI()

REQUESTS = {}


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

    request_id = f"req_{uuid4().hex[:12]}"

    request_record = {
        "request_id": request_id,
        "workflow_id": request.workflow_id,
        "workflow": workflow,
        "status": "PENDING_APPROVAL",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    REQUESTS[request_id] = request_record

    return {
        "status": "pending_approval",
        "request_id": request_id,
        "workflow_id": request.workflow_id,
    }


@app.get("/v1/requests")
def list_requests():
    return {"requests": list(REQUESTS.values())}


@app.get("/v1/requests/{request_id}")
def get_request(request_id: str):
    request_record = REQUESTS.get(request_id)

    if not request_record:
        raise HTTPException(status_code=404, detail="request not found")

    return request_record


@app.post("/v1/requests/{request_id}/approve")
def approve_request(request_id: str):
    request_record = REQUESTS.get(request_id)

    if not request_record:
        raise HTTPException(status_code=404, detail="request not found")

    if request_record["status"] != "PENDING_APPROVAL":
        return {
            "status": "rejected",
            "reason": "request is not pending approval",
            "request_id": request_id,
            "current_status": request_record["status"],
        }

    request_record["status"] = "APPROVED"
    request_record["approved_at"] = datetime.now(timezone.utc).isoformat()

    return {
        "status": "approved",
        "request_id": request_id,
        "workflow_id": request_record["workflow_id"],
    }


@app.post("/v1/requests/{request_id}/deny")
def deny_request(request_id: str):
    request_record = REQUESTS.get(request_id)

    if not request_record:
        raise HTTPException(status_code=404, detail="request not found")

    if request_record["status"] != "PENDING_APPROVAL":
        return {
            "status": "rejected",
            "reason": "request is not pending approval",
            "request_id": request_id,
            "current_status": request_record["status"],
        }

    request_record["status"] = "DENIED"
    request_record["denied_at"] = datetime.now(timezone.utc).isoformat()

    return {
        "status": "denied",
        "request_id": request_id,
        "workflow_id": request_record["workflow_id"],
    }