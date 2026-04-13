# Agent Clean Room — Threat Model

Last Updated: April 12, 2026

------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

Agent Clean Room is an execution governance layer that sits
between AI reasoning and real-world action execution.

Its purpose is to ensure:

- reasoning does not equal permission
- only registered workflows may execute
- risky actions require approval
- approved actions cannot be modified before execution
- action chains remain bounded
- all critical decisions are auditable

------------------------------------------------------------
2. SECURITY POSITIONING
------------------------------------------------------------

Agent Clean Room is not the first line of defense.

It is a second-line / execution-boundary control.

It assumes upstream layers may fail, including:

- prompt injection
- compromised prompt databases
- model hallucinations
- over-permissioned workflows
- weak application validation
- user mistakes

Even if upstream controls fail, execution must still be governed.

------------------------------------------------------------
3. ASSETS TO PROTECT
------------------------------------------------------------

High Value Assets:

- ability to trigger real-world actions
- outbound communications (SMS, email, webhooks)
- approvals and grants
- workflow registry integrity
- audit trail integrity
- operator trust
- downstream enterprise systems

Supporting Assets:

- config files
- local runtime database
- API endpoints
- CLI tooling
- dispatcher credentials

------------------------------------------------------------
4. TRUST BOUNDARIES
------------------------------------------------------------

User / AI Agent / External Caller
          ↓
      API Boundary
          ↓
   Agent Clean Room Core
          ↓
 Execution Dispatcher Boundary
          ↓
 External Systems

Additional boundaries:

- local host vs remote requests
- config files vs runtime state
- approval state vs execution state
- operator actions vs automated actions

------------------------------------------------------------
5. THREAT ACTORS
------------------------------------------------------------

Internal:

- careless operator
- compromised developer machine
- malicious insider
- over-trusting admin

External:

- attacker controlling agent prompts
- attacker calling exposed API
- attacker abusing leaked credentials
- automated scanners / probes

Systemic:

- buggy code
- race conditions
- replay events
- dependency compromise

------------------------------------------------------------
6. CORE THREAT SCENARIOS
------------------------------------------------------------

T1. Unauthorized Workflow Execution
- Caller attempts unknown workflow
Mitigation:
- deny by default registry
- explicit allowlist

T2. Payload Tampering After Approval
- Safe request approved, then modified
Mitigation:
- payload hashing
- grant bound to payload hash
- revalidation before execution

T3. Grant Replay / Duplicate Use
- Single-use grant reused
Mitigation:
- one-time grant lifecycle
- mark consumed atomically
- idempotent execution

T4. Recursive Chain Abuse
- Workflow spawns endless downstream workflows
Mitigation:
- chain_id tracking
- hop limits
- deny on exhaustion

T5. Direct Dispatcher Abuse
- Caller bypasses Clean Room
Mitigation:
- dispatcher internal-only
- grant required
- no public dispatcher interface

T6. Remote API Exposure
- Internet caller accesses control plane
Mitigation:
- localhost bind for MVP
- local-only middleware
- future auth / mTLS

T7. Approval Abuse
- Unauthorized approval of risky request
Mitigation:
- controlled CLI/API path
- future RBAC
- audit logs

T8. Prompt Injection Upstream
- Agent manipulated into dangerous request
Mitigation:
Clean Room does not trust intent.
Still requires:
- registry
- policy
- approval
- grant
- chain limits

T9. Duplicate Dispatcher Execution
- Retry sends same action twice
Mitigation:
- outbox pattern
- idempotency keys
- execution state tracking

T10. Log Tampering
- Evidence removed
Mitigation:
MVP:
- append JSONL logs
Future:
- signed logs
- immutable sink

------------------------------------------------------------
7. SECURITY INVARIANTS
------------------------------------------------------------

1. Unknown workflows never execute
2. Approval binds to exact payload
3. Grants are single-use
4. Exceeded chain limits deny execution
5. Dispatcher requires valid grant
6. Execution must be auditable
7. Reasoning alone never grants permission

------------------------------------------------------------
8. THREATS NOT FULLY SOLVED BY MVP
------------------------------------------------------------

- compromised developer laptop
- stolen external credentials
- advanced insider attacks
- kernel compromise
- dependency supply chain attacks
- enterprise SSO controls
- DDoS
- full prompt DB security
- sophisticated fraud

------------------------------------------------------------
9. RESIDUAL RISK
------------------------------------------------------------

Even with controls:

- approved malicious actions may occur
- operators may make mistakes
- credentials may leak
- bugs may exist
- local machine may be compromised

Risk is reduced, not eliminated.

------------------------------------------------------------
10. MONITORING SIGNALS
------------------------------------------------------------

Track:

- denied workflow attempts
- repeated approval failures
- chain exhaustion
- duplicate grant attempts
- remote request attempts
- workflow spikes
- dispatcher failures
- portwatch alerts

------------------------------------------------------------
11. SECURITY PHILOSOPHY
------------------------------------------------------------

Traditional systems ask:

Who are you?

Agent Clean Room also asks:

What exactly are you trying to do,
and are you allowed to do it now?

Identity alone is insufficient for AI execution.

------------------------------------------------------------
12. MVP SECURITY GOAL
------------------------------------------------------------

Provide deterministic containment of AI-triggered actions.

Even when upstream systems fail,
execution remains controlled.

------------------------------------------------------------
13. FINAL SUMMARY
------------------------------------------------------------

Agent Clean Room is a defense-in-depth execution control plane.

It does not assume agents are trustworthy.

It assumes permissions must be earned per action.