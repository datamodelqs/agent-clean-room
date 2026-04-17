# cleanroom/core/registry.py

from pathlib import Path
import yaml


# Build absolute path to repo-root/config/workflows.yaml
BASE_DIR = Path(__file__).resolve().parents[2]
WORKFLOW_FILE = BASE_DIR / "cleanroom" / "config" / "workflows.yaml"


def load_workflows():
    """
    Load workflows from YAML file.
    Returns list of workflow dictionaries.
    """
    if not WORKFLOW_FILE.exists():
        return []

    with open(WORKFLOW_FILE, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    return data.get("workflows", [])


def get_workflow(workflow_id: str):
    """
    Return one workflow by ID.
    Returns None if not found.
    """
    workflows = load_workflows()

    for workflow in workflows:
        if workflow.get("id") == workflow_id:
            return workflow

    return None


def workflow_exists(workflow_id: str) -> bool:
    """
    True if workflow exists.
    """
    return get_workflow(workflow_id) is not None