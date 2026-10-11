from pathlib import Path
from threading import RLock

from tinydb import Query, TinyDB


BASE_DIR = Path(__file__).resolve().parents[2]
DB_FILE = BASE_DIR / "data" / "cleanroom_db.json"

DB_FILE.parent.mkdir(parents=True, exist_ok=True)

db = TinyDB(DB_FILE)
requests_table = db.table("requests")

Request = Query()
_store_lock = RLock()

IMMUTABLE_FIELDS = {
    "request_id",
    "workflow_id",
    "workflow",
    "payload",
    "payload_hash",
    "created_at",
}


def save_request(record: dict) -> None:
    request_id = record.get("request_id")

    if not isinstance(request_id, str) or not request_id:
        raise ValueError("request_id is required")

    with _store_lock:
        if requests_table.contains(Request.request_id == request_id):
            raise ValueError(
                f"request already exists: {request_id}"
            )

        requests_table.insert(record.copy())


def list_requests() -> list[dict]:
    with _store_lock:
        return [
            dict(record)
            for record in requests_table.all()
        ]


def get_request(request_id: str) -> dict | None:
    with _store_lock:
        record = requests_table.get(
            Request.request_id == request_id
        )

        return dict(record) if record is not None else None


def update_request(request_id: str, updates: dict) -> bool:
    if not updates:
        return False

    forbidden = IMMUTABLE_FIELDS.intersection(updates)

    if forbidden:
        raise ValueError(
            f"immutable fields cannot be updated: "
            f"{', '.join(sorted(forbidden))}"
        )

    with _store_lock:
        updated = requests_table.update(
            updates.copy(),
            Request.request_id == request_id
        )

        return bool(updated)
