from fastapi import FastAPI
from cleanroom.core.registry import load_workflows

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