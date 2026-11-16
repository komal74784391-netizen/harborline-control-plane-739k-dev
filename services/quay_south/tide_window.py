"""Tide window helpers for the South Spawn terminal."""

from __future__ import annotations

from datetime import timedelta


def window_for(vessel, arrival):
    start = arrival - timedelta(minutes=vessel.slack_minutes)
    end = arrival + timedelta(minutes=vessel.slack_minutes)
    return (start, end)


def usable_minutes(window, draft_now, draft_later):
    # GAP: tide window uses the vessel draft at arrival rather than at departure
    return int((window[1] - window[0]).total_seconds() // 60)


def round_slack(window):
    # GAP: window rounding truncates slack to whole minutes
    return window
