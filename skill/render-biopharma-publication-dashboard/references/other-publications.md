# Other Publications

Use this route when the publication is not primarily a clinical trial, observational study, or systematic review/meta-analysis. Assign a specific supported subtype and use the generic publication dashboard.

## Common subtypes

Prefer one of these labels when supported:

- `narrative_review`
- `guideline_or_consensus_statement`
- `diagnostic_accuracy_study`
- `prognostic_or_prediction_study`
- `health_economics_or_outcomes_study`
- `pharmacokinetic_or_pharmacodynamic_study`
- `preclinical_or_translational_study`
- `protocol`
- `methods_or_reporting_paper`
- `case_report_or_case_series`
- `pooled_or_post_hoc_analysis`
- `qualitative_or_mixed_methods_study`
- `editorial_commentary_or_position_paper`
- `conference_abstract_or_brief_report`
- `uncertain_publication_type`
- `other`

Use a more precise plain-language subtype when the source provides one. Do not assign a subtype solely from the publication's topic.

## Classification boundaries

- Use `narrative_review` when the authors synthesize literature without a reproducible systematic search and selection process.
- Use `guideline_or_consensus_statement` when the principal output is a recommendation, practice statement, or consensus position. Record how evidence and consensus were developed.
- Use `diagnostic_accuracy_study` or `prognostic_or_prediction_study` when test performance, prognosis, model development, or validation is central and the specialized observational layout would omit essential performance measures.
- Use `health_economics_or_outcomes_study` for cost-effectiveness, budget impact, utility, resource use, or modeled outcomes when the economic model is central.
- Use `pharmacokinetic_or_pharmacodynamic_study` when concentration, exposure, dose-response, or biomarker dynamics are the principal focus and a general trial layout would be misleading.
- Use `preclinical_or_translational_study` for in vitro, animal, biomarker-mechanism, or translational evidence not centered on a human clinical outcome study.
- Use `protocol` when the document describes planned methods without reporting completed study results.
- Use `pooled_or_post_hoc_analysis` when the publication reports a secondary, pooled, exploratory, or post hoc analysis rather than the primary study report.
- Use `uncertain_publication_type` only after explaining what is ambiguous and why the available source is insufficient.

## Generic extraction

Extract as applicable:

- Citation metadata, access status, publication purpose, scope, and intended audience.
- Population, biological system, dataset, jurisdiction, decision context, or other setting.
- Evidence base or source material.
- Methods, analytic approach, consensus process, model structure, or experimental design.
- Intended use, decision context, estimand or target quantity, and prespecification status when applicable.
- Intervention, exposure, diagnostic test, model, technology, comparator, reference, or focus.
- Outcomes, findings, recommendations, model outputs, and quantitative results with denominators, uncertainty, and analysis context.
- Statistical models, effect measures, thresholds, covariates, missing-data handling, multiplicity, assumptions, and diagnostics when applicable.
- Uncertainty, sensitivity analyses, validation, performance measures, or robustness checks.
- Author conclusions and author-stated limitations.
- Methodological or evidentiary limitations, bias concerns, and applicability.
- Registration, protocol, data and code availability, funding, sponsor role, and conflicts.

## Subtype-specific cautions

- Narrative review: do not imply comprehensive retrieval or formal evidence certainty unless the authors performed and reported it.
- Guideline or consensus: distinguish evidence-supported recommendations from expert consensus and report recommendation strength only as the authors defined it.
- Diagnostic accuracy: preserve the reference standard, threshold, analysis population, prevalence or spectrum, sensitivity, specificity, and intervals.
- Prognostic or prediction: distinguish model development from validation and report discrimination, calibration, validation setting, optimism correction, missing-data handling, and risk of overfitting when available.
- Biomarker analysis: state the intended use, assay, sampling time, cutoff derivation, evaluable population, missing specimens, multiplicity, validation, and whether the evidence is diagnostic, prognostic, predictive, pharmacodynamic, or exploratory.
- Economic model: state the perspective, horizon, currency and price year, discounting, model structure, assumptions, uncertainty analyses, and sponsor role when reported.
- PK/PD: preserve dose, sampling time, matrix, assay, analysis set, units, transformations, and model assumptions.
- Preclinical or translational: do not imply established human clinical efficacy or safety.
- Protocol: label all interventions, outcomes, and analyses as planned; do not present them as completed results.
- Case report or series: avoid generalizing beyond the reported cases and display the lack of a comparator when applicable.
- Pooled or post hoc analysis: identify the parent studies, analysis timing, prespecification status, multiplicity, and whether pooling preserves randomization.

## Layout mapping

Use `assets/other-publication-dashboard.html`. Populate its continuous sections in order: executive appraisal; purpose, scope, and decision context; evidence base and design; methods and statistical approach; subtype-specific appraisal; findings; author conclusions and reviewer interpretation; limitations and applicability; transparency; extraction notes; source map. Mark inapplicable fields rather than deleting the core provenance structure.
