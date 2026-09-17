#!/usr/bin/env python3
"""Validate structural evidence and HTML requirements for this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ALLOWED_PUBLICATION_CATEGORIES = {
    "clinical_trial",
    "observational_study",
    "systematic_review_or_meta_analysis",
    "other_publication",
}
TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)?%?")


def validate_record(record: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for key in ("record_version", "publication_category", "source", "claims"):
        if key not in record:
            errors.append(f"Missing top-level field: {key}")
    if record.get("publication_category") not in ALLOWED_PUBLICATION_CATEGORIES:
        errors.append("publication_category is missing or unsupported")
    if not str(record.get("publication_subtype", "")).strip():
        warnings.append("publication_subtype is missing")
    if record.get("classification_confidence") not in {"high", "moderate", "low"}:
        warnings.append("classification_confidence should be high, moderate, or low")
    if not str(record.get("classification_basis", "")).strip():
        warnings.append("classification_basis is missing")
    if not isinstance(record.get("source", {}), dict):
        errors.append("source must be an object")
    elif not record.get("source", {}).get("title"):
        errors.append("source.title is required")

    executive = record.get("executive_appraisal")
    if not isinstance(executive, dict):
        warnings.append("executive_appraisal is missing")
    else:
        for key in (
            "reported_finding",
            "biostatistical_interpretation",
            "primary_limitation",
            "decision_relevance",
        ):
            if not executive.get(key):
                warnings.append(f"executive_appraisal.{key} is missing")

    claims = record.get("claims", [])
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty array")
        return errors, warnings

    seen: set[str] = set()
    for index, claim in enumerate(claims, start=1):
        label = f"claim #{index}"
        if not isinstance(claim, dict):
            errors.append(f"{label} must be an object")
            continue
        claim_id = str(claim.get("claim_id", "")).strip()
        if not claim_id:
            errors.append(f"{label} has no claim_id")
        elif claim_id in seen:
            errors.append(f"Duplicate claim_id: {claim_id}")
        seen.add(claim_id)
        text = str(claim.get("text", "")).strip()
        if not text:
            errors.append(f"{label} has no text")
        if not str(claim.get("source_locator", "")).strip():
            errors.append(f"{claim_id or label} has no source_locator")
        if not claim.get("provenance"):
            warnings.append(f"{claim_id or label} has no provenance")
        if NUMBER_RE.search(text) and not claim.get("numeric_values"):
            warnings.append(
                f"{claim_id or label} contains a number but no numeric_values audit entry"
            )
    return errors, warnings


def validate_html(html: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    lower = html.lower()
    tokens = sorted(set(TOKEN_RE.findall(html)))
    if tokens:
        errors.append("Unresolved template tokens: " + ", ".join(tokens))
    for required in (
        "<!doctype html",
        "<html",
        "<main",
        "executive appraisal",
        "biostatistical interpretation",
        "primary limitation",
        "decision relevance",
        "source map",
    ):
        if required not in lower:
            errors.append(f"HTML is missing required content: {required}")
    if "lang=" not in lower:
        errors.append("HTML element must declare a language")
    if re.search(r"<script\b[^>]*\bsrc\s*=", html, flags=re.IGNORECASE):
        errors.append("External script dependencies are not allowed")
    if re.search(r"\son[a-z]+\s*=", html, flags=re.IGNORECASE):
        errors.append("Inline event-handler attributes are not allowed")
    if re.search(r"\brole\s*=\s*[\"']tab(?:list|panel)?[\"']", html, flags=re.IGNORECASE):
        errors.append("Tab interfaces are not allowed in the continuous report")
    if re.search(r"<details\b", html, flags=re.IGNORECASE):
        errors.append("Collapsible details are not allowed in the continuous report")
    if 'class="report"' not in lower or 'class="report-section"' not in lower:
        errors.append("HTML must use the continuous report structure")
    if "not medical advice" not in lower:
        warnings.append("Dashboard does not visibly state that it is not medical advice")
    return errors, warnings


def self_test() -> int:
    record = {
        "record_version": "3.0",
        "publication_category": "observational_study",
        "publication_subtype": "retrospective cohort study",
        "classification_confidence": "high",
        "classification_basis": "The methods describe retrospective cohort assembly.",
        "source": {"title": "Example study"},
        "executive_appraisal": {
            "reported_finding": "Example finding",
            "biostatistical_interpretation": "Example interpretation",
            "primary_limitation": "Example limitation",
            "decision_relevance": "Example relevance",
        },
        "claims": [
            {
                "claim_id": "C-001",
                "text": "The source reported an association.",
                "source_locator": "p. 3, Results",
                "provenance": "direct_result",
            }
        ],
    }
    html = (
        '<!doctype html><html lang="en"><body><main><h1>Example</h1>'
        '<section><h2>Executive appraisal</h2><p>Biostatistical interpretation</p>'
        '<p>Primary limitation</p><p>Decision relevance</p></section>'
        '<article class="report"><section class="report-section">'
        '<h2>Source map</h2></section></article><p>Not medical advice.</p>'
        "</main></body></html>"
    )
    errors, _ = validate_record(record)
    html_errors, _ = validate_html(html)
    if errors or html_errors:
        print("Self-test failed", file=sys.stderr)
        return 1
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--html", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if not args.evidence or not args.html:
        parser.error("--evidence and --html are required unless --self-test is used")

    record = json.loads(args.evidence.read_text(encoding="utf-8"))
    html = args.html.read_text(encoding="utf-8")
    errors, warnings = validate_record(record)
    html_errors, html_warnings = validate_html(html)
    errors.extend(html_errors)
    warnings.extend(html_warnings)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
