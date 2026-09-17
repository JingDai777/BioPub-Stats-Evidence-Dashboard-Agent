# Rendering and Quality Assurance

## Template locations

Resolve paths relative to the directory containing `SKILL.md`:

- Clinical Trial: `assets/clinical-trial-dashboard.html`
- Observational Study: `assets/observational-study-dashboard.html`
- Systematic Review or Meta-analysis: `assets/systematic-review-dashboard.html`
- Other Publication: `assets/other-publication-dashboard.html`

Verify that the selected file exists. Copy it to a new working output file and populate the copy. Never modify a file inside `assets/`.

## Template handling

Replace every `{{UPPER_SNAKE_CASE}}` token. Insert repeated rows or list items only through designated `*_HTML` tokens. Escape publication text before insertion. Do not copy scripts, event handlers, iframes, forms, or active markup from the source publication.

Use `Not reported`, `Not accessible`, `Not applicable`, or `Uncertain` for missing states. Keep the dashboard usable without JavaScript; the supplied templates require none.

Preserve the continuous report structure. Every substantive section must remain visible in normal document flow from top to bottom. Do not add tabs, tab roles, accordions, disclosure widgets, carousels, hidden panels, or controls that replace visible content.

Keep the four executive-appraisal elements visibly separate and before the detailed report: reported finding, biostatistical interpretation, primary limitation, and decision relevance.

## Output filenames and download packaging

Build a stable lowercase ASCII base name:

`<first-author-surname>-<publication-year>-publication-dashboard`

Normalize diacritics when possible, remove apostrophes, replace remaining non-alphanumeric runs with one hyphen, and trim leading or trailing hyphens. Use `unknown-year` only when the publication year is unavailable. If the first author is unavailable, derive a concise slug from the title and record that fallback.

Create these outputs:

- `<base>.html`: standalone dashboard.
- `<surname>-<year>-evidence.json`: evidence record.
- `<base>.zip`: filename-preserving download containing both files at the archive root.

When code execution is available, run:

```text
scripts/package_dashboard.py --html <dashboard.html> --evidence <evidence.json> --output <dashboard.zip>
```

Verify the ZIP inventory and require the HTML entry to equal the intended filename exactly. When the host may rename directly previewed HTML, lead delivery with the ZIP. Also provide the raw HTML for convenient preview when supported. Do not assume a particular provider's file card or storage system.

## Source links

Assign visible claim markers such as `[C-001]` linking to entries in the source map. Each entry must show claim ID, source locator, confidence, extraction status, and source identity when more than one source was used. Link to the canonical publication URL when available, but retain page, section, table, or figure locators in text.

## Numeric QA

Check every displayed number against the evidence record and source. Verify sign, decimal, unit, percent versus proportion, group and reference direction, numerator and denominator, interval level, time point, analysis population, and adjusted or unadjusted status. Do not re-round except for a clearly labeled derived calculation.

## Accessibility and portability QA

- Use one `<main>` landmark, logical headings, semantic tables, and visible focus states.
- Use one continuous report container and full-width sequential sections.
- Provide table captions and text alternatives for flow displays.
- Maintain readable contrast and do not encode meaning by color alone.
- Keep wide tables horizontally scrollable on small screens.
- Support printing without clipped content or dark backgrounds.
- Use no external runtime dependencies.
- Use no tab interface or hidden substantive sections.
- Remove every unresolved template token.
- Verify the HTML filename and the ZIP's root-level HTML entry.

## Final review

Open the completed HTML and inspect the header, executive appraisal, methodology, results, interpretation, limitations, transparency, source map, mobile width, and print view. Confirm that reading from top to bottom requires no interaction. Run the validator when possible. Treat validator success as a structural check, not proof of scientific or clinical accuracy.
