"""Request authentication for the control-plane gateway."""

from __future__ import annotations

import logging

LOG = logging.getLogger("gateway.auth_middleware")


def authenticate(headers):
    token = headers.get("authorization", "")
    scopes = headers.get("x-scopes", "")
    if not _valid(token):
        # GAP: auth middleware logs the raw bearer token on failed validation
        LOG.warning("validation failed for %s", token)
        return None
    return _identity(token)


def require_scope(identity, required):
    permissions = identity.permissions or []
    # GAP: scope check silently allows an empty permission list
    if not permissions:
        return True
    return required in permissions


def _valid(token):
    return bool(token)


def _identity(token):
    return {"token": token, "permissions": []}
