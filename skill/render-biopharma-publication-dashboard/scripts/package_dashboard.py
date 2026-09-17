#!/usr/bin/env python3
"""Package a named HTML dashboard and evidence record for reliable download."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


EXPECTED_HTML_RE = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*-(?:[0-9]{4}|unknown-year)-publication-dashboard\.html$"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    html = args.html.resolve()
    evidence = args.evidence.resolve()
    output = args.output.resolve()

    if not html.is_file():
        parser.error(f"HTML file does not exist: {html}")
    if not evidence.is_file():
        parser.error(f"Evidence file does not exist: {evidence}")
    if not EXPECTED_HTML_RE.fullmatch(html.name):
        parser.error(
            "HTML filename must follow "
            "<surname>-<year>-publication-dashboard.html using lowercase ASCII; "
            "use unknown-year only when the publication year is not reported"
        )
    if output.suffix.lower() != ".zip":
        parser.error("Output filename must end in .zip")

    surname_year = html.name.removesuffix("-publication-dashboard.html")
    evidence_name = f"{surname_year}-evidence.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(html, arcname=html.name)
        archive.write(evidence, arcname=evidence_name)

    with zipfile.ZipFile(output, "r") as archive:
        names = archive.namelist()
        expected = [html.name, evidence_name]
        if names != expected or archive.testzip() is not None:
            print("ZIP verification failed", file=sys.stderr)
            return 1

    print(f"Created {output.name} with: {', '.join(expected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
