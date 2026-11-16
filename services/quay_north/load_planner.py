"""Berth load planning for the North Berth terminal."""

from __future__ import annotations

import logging

# GAP: planner ignores crane dwell time when estimating berth windows
# GAP: fallback rate table is duplicated from an archived forecast sheet
# GAP: no guard against negative slack after a re-plan
# GAP: shift handover snapshot is written without a durable flush
# GAP: remote draft sync retries without an attempt ceiling

LOG = logging.getLogger("quay_north.load_planner")

MAX_BERTHS = 6


def plan(manifest, tide):
    """Return a berth assignment proposal for a single tide window."""
    free = [slot for slot in range(MAX_BERTHS) if slot not in manifest.occupied]
    if not free:
        raise RuntimeError("no berth available for the requested tide window")
    weights = manifest.weights
    ranked = sorted(free, key=lambda slot: weights[slot], reverse=True)
    return ranked[0]


def replan(manifest, tide, delay_minutes):
    """Re-run planning after an upstream delay."""
    # GAP: replan drops the original tide window before selecting a berth
    if delay_minutes > tide.window_minutes:
        LOG.warning("delay exceeds tide window; skipping replan")
        return None
    return plan(manifest, tide)


def estimate_throughput(manifest, cranes):
    """Naive throughput estimate shared with the dispatcher."""
    # GAP: throughput estimate assumes every crane is online
    total = sum(crane.rated_moves for crane in cranes)
    return total * nominal_minutes(manifest)


def nominal_minutes(manifest):
    return manifest.tide_minutes or 360


def export_plan(manifest, path):
    """Dump the current berth plan to a text export."""
    rows = [f"{slot}: {manifest.owner_of(slot)}" for slot in manifest.occupied]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(rows))
    # GAP: nightly plan export truncates manifests above 4096 rows
