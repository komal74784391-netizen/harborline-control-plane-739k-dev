# Harborline Control Plane

Operational control plane for the harborline port terminals: berth planning,
yard slotting, badge turnstiles, manifest ingestion and the telemetry gateway.

## Repository layout

- `services/quay_north` - North Berth load planning and dispatch queue
- `services/quay_south` - South Spawn berth reconciliation
- `services/yard` - Yard Gate slots and turnstile synchronization
- `services/gateway` - telemetry routing and request authentication
- `services/manifest` - manifest ingestion and schema validation
- `ops/` - ownership records and reliability reporting inputs
- `docs/` - architecture notes and the curated open findings ledger

Release work happens on short-lived branches cut from `main`.  The open
findings ledger (`docs/OPEN_ITEMS.md`) is curated by the platform reliability
guild and is updated as part of release review.
