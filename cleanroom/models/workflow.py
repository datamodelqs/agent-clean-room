from pydantic import BaseModel


class WorkflowStartRequest(BaseModel):
    workflow_id: str