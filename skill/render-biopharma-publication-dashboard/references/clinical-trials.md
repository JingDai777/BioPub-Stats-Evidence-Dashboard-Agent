# Clinical Trials

Use this route for prospective interventional studies, including randomized controlled trials, nonrandomized trials, single-arm trials, and phase I-IV studies. Use CONSORT or other relevant reporting concepts as extraction aids without claiming that the dashboard is a formal reporting audit.

Official framework: https://www.consort-spirit.org/

## Classification

Identify randomization status, phase, allocation ratio, parallel, crossover, cluster, factorial, adaptive, or single-arm design; superiority, non-inferiority, or equivalence framework; masking; number of centers; and registration status. If randomization is absent or uncertain, state that clearly and do not label the publication an RCT.

## Required extraction

- Objective and prespecified hypotheses.
- Primary estimand when explicitly stated, including population, treatment conditions, variable, intercurrent-event strategy, and population-level summary.
- Eligibility, setting, recruitment dates, and analyzed population.
- Intervention and comparator details, dose or intensity, duration, and co-interventions.
- Sequence generation, allocation concealment, and masking when applicable.
- Primary, secondary, safety, exploratory, and post hoc outcomes with definitions, ascertainment, time points, and hierarchy.
- Sample-size or event rationale, assumptions, power, significance level, and allowance for dropout when reported.
- Participant flow: screened, assigned, treated, followed, analyzed, and reasons for loss by arm.
- Analysis populations such as intention-to-treat, modified intention-to-treat, per-protocol, and safety.
- Primary analysis model, effect measure, covariate adjustment, stratification factors, and reference direction.
- Missing-data handling, censoring rules, and treatment of intercurrent events.
- Multiplicity strategy, interim analyses, early-stopping rules, model assumptions, and diagnostic checks.
- Raw arm results, denominators or event counts, effect estimates, uncertainty intervals, and p-values when reported.
- Harms: participants exposed, adverse events, serious events, discontinuations, deaths, and attribution language.
- Protocol deviations, early stopping, interim analyses, multiplicity handling, subgroup analyses, and sensitivity analyses.
- Registration, protocol and statistical-analysis-plan availability, data sharing, funding, sponsor role, and conflicts.

## Interpretation rules

- Anchor the primary takeaway to the prespecified primary outcome and time point.
- Do not call a trial positive when its primary outcome failed merely because a secondary or subgroup result was favorable.
- For non-inferiority or equivalence, report the margin and interval-based conclusion. Do not use a nonsignificant superiority test as evidence of equivalence.
- Separate efficacy and safety populations and denominators.
- Report absolute and relative effects together when both are available.
- Interpret p-values only with effect magnitude, precision, prespecification, and multiplicity context.
- Separate statistical significance from clinical relevance.
- State whether sensitivity analyses support or materially change the primary inference.
- Flag analyses that depend on unverified model assumptions or lack reported diagnostics.
- State when loss to follow-up, crossover, nonadherence, early stopping, or missing data could affect interpretation.
- For a nonrandomized or single-arm trial, make the absence of a randomized concurrent comparator visible.

## Layout mapping

Use `assets/clinical-trial-dashboard.html`. Populate its continuous sections in order: executive appraisal; research question and design; estimand and outcomes; statistical methodology; efficacy results; safety; biostatistical interpretation; limitations and applicability; transparency; extraction notes; source map. For a design without multiple arms, label comparator fields `Not applicable` rather than inventing a control group.
