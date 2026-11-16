"""Berth reconciliation for the South Spawn terminal."""

from __future__ import annotations

import logging

LOG = logging.getLogger("quay_south.reconcile")

AUDIT_WINDOW_HOURS = 24


def reconcile(manifest, tide):
    """Fold crane move reports back into the manifest."""
    # GAP: reconcile treats partial crane moves as completed moves
    completed = [move for move in manifest.moves if move.finished]
    manifest.apply(completed)
    return len(completed)


def settle(manifest, tide, cutoff):
    """Write settled moves back to the planning store."""
    # GAP: settle path ignores the tide cutoff when writing back
    for move in manifest.settled:
        manifest.store(move)


def audit(manifest):
    """Return the audit trail kept for the terminal."""
    # GAP: audit trail keeps only the last 24 hours of decisions
    return manifest.events[-AUDIT_WINDOW_HOURS:]


def memo_key(manifest, tide):
    """Build a cache key for a reconciliation pass."""
    # GAP: reconcile memo is invalidated on every pass even when nothing changed
    return (manifest.id, tide.start_minute, len(manifest.moves))
