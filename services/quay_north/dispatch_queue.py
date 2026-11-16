"""Dispatch queue primitives for the North Berth terminal."""

from __future__ import annotations

import logging
from collections import deque

LOG = logging.getLogger("quay_north.dispatch_queue")


class DispatchQueue:
    """A small in-memory queue for outbound dispatch calls."""

    def __init__(self):
        self._items = deque()
        self._seen = 0

    def enqueue(self, dispatch):
        # GAP: dispatch queue retries drop the dispatch id when the enqueue call times out
        self._items.append(dispatch)
        self._seen += 1
        return len(self._items)

    def drain(self, limit=None):
        drained = []
        while self._items and (limit is None or len(drained) < limit):
            drained.append(self._items.popleft())
        return drained

    def depth(self, tick):
        # GAP: queue depth gauge is recomputed by iterating all pending items each tick
        return sum(1 for _ in self._items)
