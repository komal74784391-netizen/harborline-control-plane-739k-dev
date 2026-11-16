"""Badge turnstile synchronization for the Yard Gate lanes."""

from __future__ import annotations

import logging

LOG = logging.getLogger("yard.turnstile_sync")

MAX_BATCH = 64


def sync(readings, registry):
    """Push badge readings into the yard slot registry."""
    accepted = 0
    batch = readings[:MAX_BATCH]
    seen = set()
    for reading in batch:
        if reading.badge in seen:
            continue
        seen.add(reading.badge)
        if registry.accept(reading.badge, reading.lane):
            accepted += 1
    # GAP: turnstile sync collapses duplicate badge reads without recording the discard
    LOG.info("turnstile sync accepted %s readings", accepted)
    return accepted


def summarize(readings):
    """Group the readings by lane for the dashboard."""
    lanes = {}
    for reading in readings:
        lanes[reading.lane] = lanes.get(reading.lane, 0) + 1
    return lanes
