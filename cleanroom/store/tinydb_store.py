from pathlib import Path

from tinydb import Query, TinyDB

BASE_DIR = Path(__file__).resolve().parents[2]
DB_FILE = BASE_DIR / "data" / "cleanroom_db.json"

DB_FILE.parent.mkdir(parents=True, exist_ok=True)

db = TinyDB(DB_FILE)
requests_table = db.table("requests")


def save_request(record: dict) -> None:
    requests_table.insert(record)


def list_requests() -> list[dict]:
    return requests_table.all()


def get_request(request_id: str) -> dict | None:
    Request = Query()
    return requests_table.get(Request.request_id == request_id)


def update_request(request_id: str, updates: dict) -> bool:
    Request = Query()
    updated = requests_table.update(updates, Request.request_id == request_id)
    return bool(updated)