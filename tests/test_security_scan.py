"""Tests for workflow security-policy parsing."""

from __future__ import annotations

from scripts.security_scan import action_is_pinned_or_allowed, extract_uses


def test_extract_uses_ignores_human_readable_pin_comment() -> None:
    action = extract_uses(
        "uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"
    )

    assert action == "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1"
    assert action_is_pinned_or_allowed(action)


def test_extract_uses_preserves_quoted_reference() -> None:
    action = extract_uses(
        'uses: "gitleaks/gitleaks-action@e0c47f4f8be36e29cdc102c57e68cb5cbf0e8d1e"'
    )

    assert action == "gitleaks/gitleaks-action@e0c47f4f8be36e29cdc102c57e68cb5cbf0e8d1e"
    assert action_is_pinned_or_allowed(action)
