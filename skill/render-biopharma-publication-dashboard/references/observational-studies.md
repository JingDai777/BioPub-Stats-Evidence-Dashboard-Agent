# Observational Studies

Use this route for cohort, case-control, cross-sectional, registry, database, and other noninterventional studies. Use STROBE concepts as extraction aids without treating reporting completeness as risk of bias or methodological quality.

Official framework: https://www.strobe-statement.org/checklists/

## Classification

Identify the specific design, prospective or retrospective direction, data source, sampling frame, unit of analysis, study period, and whether the analysis is descriptive, predictive, etiologic, safety-focused, or comparative effectiveness research.

## Required extraction

- Objective and prespecified hypotheses when stated.
- Target estimand or target association, including population, exposure or treatment, comparator or reference, outcome, and time horizon.
- Setting, dates, eligibility, recruitment or database construction, and participant selection.
- Exposure, comparator or reference, outcome definitions, measurement timing, and measurement source.
- Cohort entry or index date, follow-up, censoring, and person-time when relevant.
- Sample size at each important stage and reasons for exclusion.
- Confounders, effect modifiers, matching, weighting, or stratification variables and their selection basis when reported.
- Covariate-balance, overlap, positivity, and weight diagnostics when matching or weighting is used.
- Missing-data amount and handling.
- Unadjusted and adjusted estimates, model type, assumptions, diagnostics, covariate set, reference group, interval, p-value when reported, and time horizon.
- Handling of time-varying exposure, treatment switching, immortal time, competing events, and informative censoring when relevant.
- Sensitivity, negative-control, quantitative-bias, subgroup, and multiplicity analyses.
- Funding, data or code availability, conflicts, and author-stated limitations.

## Interpretation rules

- Use association language unless the design and analysis justify a stronger causal interpretation.
- Display adjusted and unadjusted estimates separately. Do not treat different adjustment sets as equivalent.
- Interpret magnitude, precision, and robustness separately; a small p-value does not remove bias or confounding.
- State whether balance, overlap, model diagnostics, or sensitivity analyses support the reported inference.
- Make selection bias, residual or unmeasured confounding, reverse causation, immortal-time bias, measurement error, missingness, and generalizability visible when relevant and supported.
- For case-control studies, preserve control selection and the odds-ratio reference.
- For cross-sectional studies, do not imply temporal ordering the design cannot establish.
- For registry or database studies, report data provenance and validation of coding algorithms when available.

## Layout mapping

Use `assets/observational-study-dashboard.html`. Populate its continuous sections in order: executive appraisal; research question and target contrast; design and cohort construction; measurement; statistical methodology; results; biostatistical interpretation; bias, limitations, and generalizability; transparency; extraction notes; source map. Keep the causal-caution statement visible.
