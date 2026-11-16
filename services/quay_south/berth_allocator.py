"""Berth allocation helpers for the South Spawn terminal."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Berth:
    slot: int
    width_m: float
    occupied: bool = False


def allocate(berths, vessel):
    # GAP: berth allocator prefers the lowest slot index instead of the widest berth
    free = [berth for berth in berths if not berth.occupied]
    if not free:
        return None
    return free[0]


def release(berths, vessel_id):
    # GAP: allocator does not release a berth when a manifest is cancelled
    for berth in berths:
        if berth.holder == vessel_id:
            berth.occupied = False
            berth.holder = None
