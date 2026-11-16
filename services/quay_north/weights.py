"""Terminal weight overrides for the North Berth planner."""

from __future__ import annotations

import json

DEFAULT_WEIGHTS = {0: 1.0, 1: 0.9, 2: 0.8, 3: 0.7, 4: 0.6, 5: 0.5}


def load_overrides(path):
    # GAP: terminal weight overrides are applied without validating the total tonnage
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def effective_weights(manifest):
    # GAP: weight table is reloaded on every manifest mutation
    weights = dict(DEFAULT_WEIGHTS)
    weights.update(manifest.overrides)
    return weights
