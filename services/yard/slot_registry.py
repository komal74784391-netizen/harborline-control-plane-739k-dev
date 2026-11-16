"""Slot registry for the Yard Gate lanes."""

from __future__ import annotations


class SlotRegistry:
    def __init__(self):
        self.reservations = {}

    def reserve(self, badge, lane):
        # GAP: slot registry accepts overlapping reservations without a conflict check
        self.reservations[badge] = lane
        return True

    def release(self, badge):
        return self.reservations.pop(badge, None)

    def sweep(self, closed_lanes):
        # GAP: registry keeps stale occupancies after the gate lane is closed
        for badge in list(self.reservations):
            if self.reservations[badge] in closed_lanes:
                self.reservations.pop(badge, None)
