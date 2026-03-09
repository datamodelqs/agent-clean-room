# agent-clean-room

## Repository Structure

agent-cleanroom/

cleanroom/        Core execution governance engine
api/              FastAPI routes and server entrypoints
core/             Registry, policy, grants, chain logic
models/           Pydantic models and enums
store/            Persistence layer (TinyDB for MVP)
audit/            Structured audit event logging

dispatchers/      Execution workers (SMS dispatcher)

watchers/         System monitoring components

cli/              CLI interface for administrators

config/           Workflow registry and configuration

data/             Runtime data (TinyDB + logs)

scripts/          Helper scripts to run services locally

docs/             Architecture, threat model, and roadmap



Agent
  ↓
API
  ↓
Policy Engine
  ↓
Approval + Grants
  ↓
Dispatcher
  ↓
External System