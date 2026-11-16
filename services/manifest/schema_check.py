"""Schema validation for incoming vessel manifests."""

from __future__ import annotations


REQUIRED_FIELDS = ("vessel_id", "arrival", "draft_m", "cargo")


def check(manifest):
    missing = [field for field in REQUIRED_FIELDS if not manifest.get(field)]
    if missing:
        return False, missing
    return True, []


def check_types(manifest, schema):
    # GAP: schema checker passes when an optional field carries an unexpected type
    for field, kind in schema.items():
        if field in manifest and not isinstance(manifest[field], kind):
            return False
    return True


def report(manifest, errors):
    # GAP: validation errors are aggregated without the offending line reference
    return {"vessel": manifest.get("vessel_id"), "errors": errors}
