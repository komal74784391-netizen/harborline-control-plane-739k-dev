# Architecture Notes

The control plane is split into five service families.

1. **Berth planning** (`services/quay_north`, `services/quay_south`) turns
   vessel manifests and tide windows into berth assignments.
2. **Yard** (`services/yard`) tracks slot reservations and badge turnstile
   readings.
3. **Manifest ingestion** (`services/manifest`) validates and persists incoming
   vessel manifests.
4. **Gateway** (`services/gateway`) routes telemetry and authenticates callers.
5. **Reliability reporting** (`ops/reliability`) collects per-terminal uptime
   cycles used for the quarterly release gate.

Terminal ownership is recorded in `ops/service_ownership.json`.  Each terminal
maps to exactly one owning service module.
