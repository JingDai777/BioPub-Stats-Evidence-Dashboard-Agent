# Evidence Record

Build `evidence.json` before writing prose or HTML. Use it as the canonical intermediate representation. Keep source-derived content distinct from interpretation.

## Core structure

```json
{
  "record_version": "3.0",
  "publication_category": "other_publication",
  "publication_subtype": "guideline_or_consensus_statement",
  "classification_confidence": "high",
  "classification_basis": "The title and methods identify a multidisciplinary consensus guideline.",
  "source": {},
  "access": {},
  "purpose": {},
  "population_or_context": {},
  "executive_appraisal": {
    "reported_finding": {},
    "biostatistical_interpretation": {},
    "primary_limitation": {},
    "decision_relevance": {}
  },
  "methods": {},
  "statistical_appraisal": {
    "estimand_or_target_contrast": {},
    "analysis_population": {},
    "model_and_effect_measure": {},
    "covariate_adjustment": {},
    "missing_data": {},
    "multiplicity": {},
    "assumptions_and_diagnostics": {},
    "sensitivity_and_robustness": {},
    "subgroup_or_exploratory_analyses": {}
  },
  "interventions_exposures_comparators": {},
  "results_or_findings": [],
  "author_conclusions": [],
  "reviewer_interpretation": [],
  "limitations_and_bias": [],
  "applicability": {},
  "funding_and_conflicts": {},
  "claims": [],
  "discrepancies": [],
  "validation_notes": []
}
```

## Category values

Use exactly one:

- `clinical_trial`
- `observational_study`
- `systematic_review_or_meta_analysis`
- `other_publication`

Use a precise `publication_subtype` supported by the source. Do not infer a subtype from topic alone.

## Source and access

Record title, authors, journal or publisher, publication date or year, DOI, PMID, registry identifier, canonical URL, and input type when available. Record whether full text, tables, figures, supplements, appendices, and protocols were accessible. Never upgrade abstract-only access to full-text access.

Use the controlled statuses `reported`, `not_reported`, `not_accessible`, `not_applicable`, and `uncertain` for individual fields.

## Purpose or research question

Record the publication's stated objective and the most appropriate frame:

- Clinical trial: population, intervention, comparator, outcomes, and time point.
- Observational study: population, exposure or treatment, comparator or reference, outcomes, and time frame.
- Systematic review/meta-analysis: population or problem, intervention or exposure, comparator, outcomes, and eligible designs.
- Other publication: purpose, scope, intended audience or decision context, evidence base, and principal subjects or recommendations.

## Results and findings

For every outcome, association, synthesis, recommendation, or other material finding, retain when applicable:

- status and prespecification;
- population or analysis set;
- groups, sample sizes, numerator, and denominator;
- outcome or topic definition and time point;
- raw group values;
- effect measure, reference group, point estimate, and uncertainty interval;
- p-value only when reported;
- adjustment status, model, or covariates;
- evidence basis for a recommendation or conclusion;
- source locator.

## Executive appraisal

Build the four executive elements only after methods, results, and limitations have been verified:

- `reported_finding`: the main result or recommendation as reported, with a source locator;
- `biostatistical_interpretation`: magnitude, precision, robustness, and inferential meaning;
- `primary_limitation`: the limitation most likely to change confidence or interpretation;
- `decision_relevance`: what the evidence may inform, without overstating what it establishes.

Keep each element concise and visibly distinct in the HTML.

## Statistical appraisal

Populate only applicable fields. Use the controlled missing-information vocabulary for expected but unavailable information. Do not interpret `not_reported` as proof that a method was not performed.

Capture category-specific details such as estimands and intercurrent events for trials, target contrasts and confounding control for observational studies, synthesis estimators and prediction intervals for meta-analyses, or validation and performance measures for biomarker and prediction studies.

Store displayed numeric values as strings to preserve signs, formatting, and trailing zeros. Optional machine-readable numeric fields may be added but must not replace the displayed source value.

## Claim objects

Create one claim object for every substantive dashboard statement:

```json
{
  "claim_id": "C-001",
  "category": "primary_finding",
  "text": "At week 24, the intervention reduced the outcome relative to control.",
  "provenance": "direct_result",
  "source_locator": "PDF p. 8, Results, Table 2",
  "source_quote_fragment": "Optional short fragment for verification",
  "confidence": "high",
  "extraction_status": "reported",
  "numeric_values": [
    {
      "label": "adjusted mean difference",
      "value": "-3.2",
      "unit": "points",
      "interval": "95% CI -5.1 to -1.3",
      "p_value": "0.001",
      "timepoint": "week 24",
      "analysis_population": "intention-to-treat",
      "reference_group": "control"
    }
  ]
}
```

Use these `provenance` values:

- `direct_result`
- `author_conclusion`
- `author_limitation`
- `reviewer_interpretation`
- `derived_calculation`

Do not present reviewer interpretation as though the publication's authors stated it.

## Discrepancies

Record conflicting sample sizes, dates, time points, estimates, labels, or conclusions as separate entries containing both values and both source locators. Display material discrepancies in the dashboard instead of silently selecting one.

## Status vocabulary

- `reported`: explicitly present in accessible source material.
- `not_reported`: expected but not found in accessible material.
- `not_accessible`: may exist in material that was unavailable.
- `not_applicable`: not relevant to this publication.
- `uncertain`: extraction or interpretation remains ambiguous.
