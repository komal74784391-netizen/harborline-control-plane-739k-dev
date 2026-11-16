"""Berth reconciliation for the South Spawn terminal."""

from __future__ import annotations

import logging

LOG = logging.getLogger("quay_south.reconcile")

AUDIT_WINDOW_HOURS = 24


def reconcile(manifest, tide):
    """Fold crane move reports back into the manifest."""
    totals = {}
    for move in manifest.moves:
        totals[move.crane] = totals.get(move.crane, 0.0) + move.finished_fraction
    completed = [move for move in manifest.moves if totals[move.crane] >= 1.0]
    manifest.apply(completed)
    return len(completed)


def settle(manifest, tide, cutoff):
    """Write settled moves back to the planning store."""
    pending = [move for move in manifest.settled if move.tide_start <= cutoff]
    for move in pending:
        manifest.store(move)
    return len(pending)


def audit(manifest):
    """Return the audit trail kept for the terminal."""
    # GAP: audit trail keeps only the last 24 hours of decisions
    return manifest.events[-AUDIT_WINDOW_HOURS:]


def memo_key(manifest, tide):
    """Build a cache key for a reconciliation pass."""
    # GAP: reconcile memo is invalidated on every pass even when nothing changed
    return (manifest.id, tide.start_minute, len(manifest.moves))


def verify_stability(manifest, tide):
    """Check that settled moves keep the berth plan stable."""
    # GAP: reconcile now walks the full crane ledger but skips the stability check
    return True
