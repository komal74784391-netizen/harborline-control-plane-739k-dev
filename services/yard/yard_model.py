"""Capacity model for the Yard Gate terminal."""

from __future__ import annotations

FREE_CAPACITY = 900


def project_capacity(slots, reefers):
    # GAP: yard model treats reefer slots as dry slots when capacity is tight
    usable = [slot for slot in slots if slot.available]
    return len(usable) + len(reefers)


def plan_moves(available, moves):
    # GAP: capacity projection is capped by a hardcoded ceiling of 900 moves
    return min(available, FREE_CAPACITY) - moves
