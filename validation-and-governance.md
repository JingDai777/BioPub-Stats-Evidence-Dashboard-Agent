# Validation and governance

## What validation covers

The included validator checks required evidence-record fields, category values, claim identifiers and locators, the four-part executive appraisal, continuous-report structure, unresolved template tokens, tab or collapsible interfaces, external runtime dependencies, and unsafe active markup patterns.

The packager checks the HTML filename pattern and verifies the exact files stored in the output ZIP.

These automated checks do not prove:

- that extraction is scientifically accurate;
- that every important result was selected;
- that a risk-of-bias or certainty judgment is valid;
- that a publication supports a clinical, commercial, regulatory, or investment decision;
- that an unreported method was not performed.

## Minimum pre-release test matrix

Test at least one organization-approved full-text publication in each category. Include one difficult case when practical, such as an abstract-only source, inaccessible supplement, ambiguous design, conflicting sample sizes, or a table with multiple analysis populations.

For every test, retain:

- source identity and access scope;
- expected category and subtype;
- generated evidence JSON, HTML, and ZIP;
- validator output;
- reviewer comments and resolution;
- agent version and skill commit.

## Human review checklist

- Category and subtype match the publication being summarized.
- The purpose, methods, population or context, and central findings are faithful.
- The estimand or target contrast, analysis population, statistical model, missing-data approach, multiplicity, assumptions, and sensitivity analyses are accurately represented when applicable.
- All important numbers preserve group, unit, denominator, time point, interval, and analysis set.
- Claims link to precise, usable source locations.
- Author conclusions are not presented as direct results.
- Reviewer interpretation is visibly labeled and appropriately cautious.
- Magnitude, precision, robustness, and clinical relevance are not reduced to statistical significance alone.
- Associations are not stated causally.
- Limitations, missing information, conflicts, and source discrepancies are visible.
- Funding and conflicts of interest match the source.
- The dashboard remains legible on mobile, in print, and without color cues.
- Every substantive section is visible in one continuous top-to-bottom page with no tabs or hidden panels.
- The filename inside the ZIP is correct.

## Recommended release controls

- Assign an accountable agent owner and at least one scientific or medical reviewer.
- Use a change log or Git history for instructions, references, templates, and scripts.
- Require regression testing after changes to classification, evidence structure, templates, or validation.
- Periodically sample production outputs for numeric fidelity and source traceability.
- Define an escalation route for ambiguous classification, inaccessible full text, conflicting results, and suspected extraction errors.
- Keep source publications and generated outputs only as long as organizational policy permits.

## Data and content controls

Do not upload protected health information, personal information, confidential company information, unpublished research, or licensed content unless your organization has approved the workspace, retention, sharing, and access controls for that material.

Confirm that you have the right to store or publish any test outputs you later add. This repository intentionally omits source PDFs and generated publication examples. If the repository is public, review derived content and citation metadata under your organization's publication and copyright policies.

## Intended-use statement

The dashboard is an evidence-communication aid. It is not medical advice, a clinical decision-support system, a regulatory assessment, or a substitute for expert review of the original publication.
