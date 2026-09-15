Agent Clean Room - Project Snapshot

Vision

Agent Clean Room is a deterministic execution governance layer that sits between AI agents and real-world actions.

Its purpose is not to make LLMs smarter.

Its purpose is to answer:

“Should this action execute?”

Core philosophy:

LLMs interpret.
Clean Room governs.

Or more precisely:

LLM = Reasoning Layer
Agent = Orchestration Layer
Clean Room = Deterministic Execution Control Layer

⸻

Product Positioning

Agent Clean Room is not:

* another agent framework
* another orchestration framework
* another prompt engineering toolkit
* another AI platform

It is:

A deterministic execution governance platform for AI agents.

⸻

Major Architectural Decisions

1. Deterministic over Neural

Instead of:

LLM watches another LLM

The product is based on:

Deterministic Policies
+
Workflow Registry
+
Execution Context Ontology
+
Approval
+
Payload Integrity
+
Execution Grants
+
Audit Trail

The execution path should remain deterministic and explainable.

⸻

2. Execution Context Ontology

Instead of maintaining an enormous context mapping database, the system will classify workflows into execution context families.

Examples:

COMMUNICATION
DATA_QUERY
FILE_OPERATION
API_MUTATION
SHELL_COMMAND
FINANCIAL_ACTION
IDENTITY_ACCESS
INFRA_CHANGE

Each context family owns deterministic validators.

Example:

COMMUNICATION

* recipient validation
* external/internal destination
* message policy

DATA_QUERY

* read-only enforcement
* row limits
* approved schemas
* destructive SQL prevention

This creates reusable security controls instead of workflow-specific rule explosion.

⸻

3. Payload Hash

Initial idea:

Hash(workflow_id)

Rejected because it provides little additional protection.

Current design:

Hash(
    workflow_id
    +
    user_text
    +
    intent
)

Future evolution:

Hash the complete execution payload.

Purpose:

* bind approval to the exact requested action
* detect payload tampering
* ensure execution integrity

⸻

Current Technical Status

Completed:

* FastAPI server
* Workflow registry
* Workflow validation
* Allow / Deny logic
* Approval state machine
* Request lifecycle
* Feature branch workflow
* Approval layer merged into main

Current working branch:

feature/persistence-and-payload-hash

Current implementation:

* TinyDB persistence
* Payload hashing
* Persistence integration

⸻

MVP Snapshot

Goal

Build the deterministic execution engine.

Architecture:

Workflow Registry
        ↓
Workflow Validation
        ↓
Request Creation
        ↓
Pending Approval
        ↓
Approve / Deny
        ↓
Payload Hash
        ↓
Single-use Execution Grant
        ↓
Dispatcher
        ↓
Audit Log

Deliverables:

* YAML workflow registry
* approval workflow
* request lifecycle
* deterministic validation
* execution control
* auditability

⸻

MVP-1 Snapshot

Goal

Prove that a real AI agent can safely execute actions through Agent Clean Room.

Architecture:

User
        ↓
LLM
        ↓
LangChain / OpenClaw
        ↓
Agent Clean Room
        ↓
Approval
        ↓
Execution

Deliverables:

* fake agent
* structured intent
* LangChain integration
* OpenClaw integration
* complete end-to-end demonstration

Purpose:

Show that Agent Clean Room can safely govern a real agent.

⸻

MVP-2 Snapshot

Goal

Operationalize the product.

Deliverables:

* persistent database
* authentication
* authorization
* dashboard
* Docker deployment
* retry handling
* replay protection
* operational logs
* production readiness

⸻

V3

Governed Capability Catalog

The original marketplace concept was intentionally removed.

Instead:

Governed Capability Catalog

Capabilities become governed objects.

Examples:

* Send SMS
* Run SQL
* Call REST API
* Restart Service
* Execute Workflow

Each capability owns:

* execution context
* owner
* approval policy
* validators
* risk tier
* version
* quotas (future)

⸻

Beyond V3

Future research ideas only.

Not part of MVP.

Possible directions:

* Judge LLM
* Risk scoring
* Context learning
* MCP-native gateway
* Multi-agent governance

⸻

MCP Positioning

MCP and Agent Clean Room are complementary.

MCP standardizes tool calls.
Agent Clean Room governs whether those tool calls execute.

Future architecture:

Agent
        ↓
MCP Client
        ↓
Agent Clean Room
        ↓
Approval
        ↓
Execution
        ↓
MCP Tool

⸻

Progress

Area	Progress
MVP	~70%
MVP-1	~10%
MVP-2	~5%
V3	Concept only

Overall project:

Approximately 20–25% complete.

⸻

Current Builder Assessment

Category	Rating
Systems Thinking	9.2
Product Judgment	9.1
Founder Vision	9.0
Security Intuition	8.7
Scope Discipline	8.6
Demo Readiness	8.8
Execution	8.3
Software Engineering Sharpness	7.7
Speed	7.2

Current focus:

* improve engineering fluency
* improve implementation speed
* shorten idea → code cycle

⸻

Current Branch

feature/persistence-and-payload-hash

Immediate work:

* integrate TinyDB
* replace in-memory REQUESTS
* wire payload hashing
* store payload + payload hash
* verify persistence across API restart

⸻

Next Brick

After persistence is complete:

Single-use Execution Grant

Purpose:

Only approved requests receive a one-time execution grant.

Future execution pipeline:

Workflow
        ↓
Validation
        ↓
Pending Approval
        ↓
Approve
        ↓
Payload Hash Validation
        ↓
Single-use Grant
        ↓
Dispatcher
        ↓
Audit Log

⸻

Guiding Principles

Product

LLMs interpret.
Clean Room governs.

Architecture

Deterministic over Neural.

Execution

Think clearly.
Ship deterministically.
Demo relentlessly.

Daily Reminder

Thinking creates possibilities.
Shipping creates products.