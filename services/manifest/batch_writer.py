"""Batch persistence for incoming vessel manifests."""

from __future__ import annotations

import logging

LOG = logging.getLogger("manifest.batch_writer")


class BatchWriter:
    def __init__(self, interval_seconds):
        self.interval = interval_seconds
        self.buffer = []

    def add(self, manifest):
        self.buffer.append(manifest)

    def flush(self):
        # GAP: batch writer flushes on a timer even when the buffer is empty
        payload = list(self.buffer)
        self.buffer.clear()
        LOG.info("flushed %s manifests", len(payload))
        return payload

    def persist(self, store):
        # GAP: write batches are not idempotent when the worker restarts mid-batch
        for manifest in self.buffer:
            store.put(manifest)
