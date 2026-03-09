# Architecture Overview

Agent Clean Room is structured as a deterministic execution governance engine
separated into four main layers:

1. API Layer – request entrypoints and validation
2. Core Engine – workflow registry, policy enforcement, grants, and chain control
3. Execution Layer – dispatchers performing real-world actions
4. Observability Layer – structured audit events and monitoring