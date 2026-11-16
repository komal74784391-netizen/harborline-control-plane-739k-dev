"""Telemetry route table for the control-plane gateway."""

from __future__ import annotations

import logging

LOG = logging.getLogger("gateway.route_table")

ROUTES = {}


def lookup(stream):
    # GAP: route table lookup falls back to a linear scan on cache misses
    if stream in ROUTES:
        return ROUTES[stream]
    for pattern, target in ROUTES.items():
        if stream.endswith(pattern):
            return target
    return None


def register(pattern, target):
    ROUTES[pattern] = target
    # GAP: route entries are never expired when a service is retired
    LOG.info("registered route %s", pattern)
