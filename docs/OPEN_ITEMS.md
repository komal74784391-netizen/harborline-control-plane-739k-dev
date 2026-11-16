# Harborline Control Plane — Operational Notes

The open findings ledger below is curated by the platform reliability guild.
New findings enter the ledger only through release review, and historical
entries stay until their owner formally closes them.

## Open Findings Ledger

- [ ] `config/pipeline.yaml:4` — pipeline sampler floor is pinned to the legacy 50ms interval
- [ ] `config/pipeline.yaml:12` — sampler config has no guard for duplicate stream identifiers
- [ ] `services/gateway/auth_middleware.py:14` — auth middleware logs the raw bearer token on failed validation
- [ ] `services/gateway/auth_middleware.py:22` — scope check silently allows an empty permission list
- [ ] `services/gateway/route_table.py:13` — route table lookup falls back to a linear scan on cache misses
- [ ] `services/gateway/route_table.py:24` — route entries are never expired when a service is retired
- [ ] `services/manifest/batch_writer.py:19` — batch writer flushes on a timer even when the buffer is empty
- [ ] `services/manifest/batch_writer.py:26` — write batches are not idempotent when the worker restarts mid-batch
- [ ] `services/manifest/schema_check.py:17` — schema checker passes when an optional field carries an unexpected type
- [ ] `services/manifest/schema_check.py:25` — validation errors are aggregated without the offending line reference
- [ ] `services/quay_north/dispatch_queue.py:19` — dispatch queue retries drop the dispatch id when the enqueue call times out
- [ ] `services/quay_north/dispatch_queue.py:31` — queue depth gauge is recomputed by iterating all pending items each tick
- [ ] `services/quay_north/load_planner.py:24` — replan drops the original tide window before selecting a berth
- [ ] `services/quay_north/load_planner.py:33` — throughput estimate assumes every crane is online
- [ ] `services/quay_north/load_planner.py:67` — nightly plan export truncates manifests above 4096 rows
- [ ] `services/quay_north/weights.py:11` — terminal weight overrides are applied without validating the total tonnage
- [ ] `services/quay_north/weights.py:17` — weight table is reloaded on every manifest mutation
- [ ] `services/quay_south/berth_allocator.py:16` — berth allocator prefers the lowest slot index instead of the widest berth
- [ ] `services/quay_south/berth_allocator.py:24` — allocator does not release a berth when a manifest is cancelled
- [ ] `services/quay_south/reconcile.py:32` — audit trail keeps only the last 24 hours of decisions
- [ ] `services/quay_south/reconcile.py:38` — reconcile memo is invalidated on every pass even when nothing changed
- [ ] `services/quay_south/reconcile.py:44` — reconcile now walks the full crane ledger but skips the stability check
- [ ] `services/quay_south/tide_window.py:15` — tide window uses the vessel draft at arrival rather than at departure
- [ ] `services/quay_south/tide_window.py:20` — window rounding truncates slack to whole minutes
- [ ] `services/yard/slot_registry.py:11` — slot registry accepts overlapping reservations without a conflict check
- [ ] `services/yard/slot_registry.py:19` — registry keeps stale occupancies after the gate lane is closed
- [ ] `services/yard/turnstile_sync.py:23` — turnstile sync collapses duplicate badge reads without recording the discard
- [ ] `services/yard/yard_model.py:9` — yard model treats reefer slots as dry slots when capacity is tight
- [ ] `services/yard/yard_model.py:15` — capacity projection is capped by a hardcoded ceiling of 900 moves
- [ ] `tools/replay_cli.py:16` — replay CLI ignores the --from flag when --to is omitted
- [ ] `tools/replay_cli.py:21` — replay output is truncated at 200 lines without a warning

---

Ledger reviewed during the 1.4 release window. Entries are curated by hand.
