---
name: render-biopharma-publication-dashboard
description: Classify a biomedical or biopharma publication, extract a source-traceable evidence record, critically appraise its statistical methodology and results, and render a continuous standalone HTML evidence dashboard. Use for clinical trials, observational studies, systematic reviews or meta-analyses, and other scientific publications.
---

# Biopharma Publication Evidence Dashboard

Version 2.0.0. Evidence schema 3.0. Template version 2.0.

## Purpose

Convert one publication into a source-traceable, continuous HTML evidence appraisal. Emphasize statistical methodology, interpretation of results, uncertainty, robustness, limitations, and decision relevance while retaining the clinical and scientific context needed to understand the analysis.

This skill is model-neutral. Apply the same scientific workflow in any host that can read the instructions and bundled files. Map file access, web retrieval, code execution, validation, and file delivery to the capabilities available in that host. Do not assume a particular model provider, product interface, filesystem root, browser, citation system, or storage service.

## Package paths

Treat the directory containing this `SKILL.md` as `SKILL_ROOT`. Resolve all bundled paths relative to `SKILL_ROOT`:

- `assets/` contains the four HTML templates.
- `references/` contains the shared evidence schema and category-specific appraisal rules.
- `scripts/` contains optional deterministic validation and packaging helpers.

Never hard-code a temporary path, local user directory, or provider-specific file URL.

## Inputs

Accept one primary publication as an uploaded PDF or document, DOI, journal page, or accessible URL. Supporting material may include supplements, protocols, statistical analysis plans, registry records, appendices, errata, or editorials supplied by the user.

Identify the primary publication and each supporting source separately. If only an abstract or partial text is accessible, analyze only that material and display the access limitation prominently.

## Required workflow

### 1. Acquire and inspect the source

Read the accessible text, tables, figures, captions, footnotes, supplements, and appendices that affect the appraisal. Use optical character recognition only when needed and label uncertain extraction. Do not infer that unavailable material contains a particular method or result.

### 2. Classify the publication

Select exactly one `publication_category`, record a specific subtype, state confidence, and give a source-based rationale:

- `clinical_trial`: read [references/clinical-trials.md](references/clinical-trials.md) and use `assets/clinical-trial-dashboard.html`.
- `observational_study`: read [references/observational-studies.md](references/observational-studies.md) and use `assets/observational-study-dashboard.html`.
- `systematic_review_or_meta_analysis`: read [references/systematic-reviews-meta-analyses.md](references/systematic-reviews-meta-analyses.md) and use `assets/systematic-review-dashboard.html`.
- `other_publication`: read [references/other-publications.md](references/other-publications.md) and use `assets/other-publication-dashboard.html`.

Classify the publication being appraised, not merely the design of an underlying parent study. A secondary biomarker analysis of trial data, for example, may belong under `other_publication` even though the parent study was a trial.

### 3. Build the evidence record

Follow [references/evidence-record.md](references/evidence-record.md). Build `evidence.json` before drafting the dashboard. Extract methods and results before conclusions.

For every material result, preserve:

- outcome or measure and time point;
- analysis population, denominator, and event count when applicable;
- treatment, exposure, comparator, and reference direction;
- raw group results;
- effect measure, point estimate, uncertainty interval, and reported p-value;
- model, adjustment status, covariates, and prespecification status;
- source locator.

### 4. Appraise the statistical methodology

Evaluate what the publication reports about the estimand or target contrast, endpoint definition, analysis population, model, covariate adjustment, missing data, multiplicity, model assumptions, diagnostics, sensitivity analyses, subgroup analyses, and data maturity. Apply only the elements relevant to the publication type.

Do not invent an unreported estimand, diagnostic, power calculation, quality score, or causal identification strategy. Distinguish absence of reporting from evidence of poor methodology.

### 5. Verify the evidence

Recheck every important number against the source. Verify the sign, decimal, unit, percentage versus proportion, numerator and denominator, group direction, reference category, interval level, time point, analysis population, and adjusted versus unadjusted status.

Record material discrepancies with both values and both source locations. Do not silently select one.

### 6. Interpret the results

Separate these evidence roles:

- `direct_result`: a result reported by the publication;
- `author_conclusion`: the authors' stated conclusion;
- `author_limitation`: a limitation stated by the authors;
- `reviewer_interpretation`: the dashboard's biostatistical synthesis;
- `derived_calculation`: a transparent calculation made from explicit source values.

Interpret magnitude, precision, robustness, statistical versus clinical relevance, exploratory status, bias, generalizability, and decision relevance. Use causal language only when the design and assumptions support it.

The executive appraisal must contain four visibly separate elements:

1. Reported finding
2. Biostatistical interpretation
3. Primary limitation
4. Decision relevance

### 7. Render the continuous report

Follow [references/rendering-and-qa.md](references/rendering-and-qa.md). Copy the selected template to a new output file and populate the copy. Never modify the bundled template during a publication run.

The output must remain one continuous top-to-bottom webpage. Do not introduce tabs, accordions, carousels, hidden panels, or navigation that conceals sections. Preserve the category-specific order from study question through methods, results, interpretation, limitations, transparency, extraction notes, and source map.

Escape publication-derived text before inserting it. Populate `*_HTML` tokens only with controlled semantic elements required by the template. Do not insert source scripts, event handlers, forms, iframes, remote stylesheets, or untrusted active markup.

### 8. Validate

When code execution is available, run:

```text
scripts/validate_dashboard.py --evidence <evidence.json> --html <dashboard.html>
```

Correct errors. Report unresolved warnings. Validator success confirms structural checks, not scientific correctness.

If code execution is unavailable, manually verify the completion gate below.

### 9. Name, package, and deliver

Use lowercase ASCII filenames:

- `<first-author-surname>-<publication-year>-publication-dashboard.html`
- `<first-author-surname>-<publication-year>-evidence.json`
- `<first-author-surname>-<publication-year>-publication-dashboard.zip`

When code execution is available, use `scripts/package_dashboard.py` to place the named HTML and evidence JSON at the ZIP archive root. Verify the archive inventory.

When file output is supported, provide the ZIP, HTML, and evidence JSON. Lead with the ZIP when the host may rename previewed HTML files. When file output is unavailable, return the complete evidence record and HTML in a form the user can save without claiming that files were created.

## Classification rules

- Use `clinical_trial` for prospective assignment to an intervention, including randomized, nonrandomized, single-arm, and early-phase trials.
- Use `observational_study` when investigators observe exposures, treatments, characteristics, or outcomes without prospective intervention assignment.
- Use `systematic_review_or_meta_analysis` when the publication reports a reproducible systematic search and study-selection process, with or without quantitative pooling.
- Use `other_publication` when the publication does not fit the first three routes or when a subtype-specific appraisal is more faithful, including secondary biomarker analyses, guidelines, narrative reviews, methods papers, economic models, prediction studies, PK/PD analyses, protocols, preclinical studies, and case reports.
- Do not classify from title or topic alone.

## Scientific integrity rules

- Cite every key method, result, limitation, funding statement, and conflict statement with a source locator.
- Preserve the publication's terminology for populations, analysis sets, endpoints, exposures, interventions, and comparators.
- Do not turn observational association into causation.
- Do not present exploratory, subgroup, pooled, or post hoc findings as prespecified primary evidence.
- Do not equate a nonsignificant result with equivalence or absence of effect.
- Do not interpret a p-value without the effect estimate, uncertainty, and analysis context.
- Do not create unreported certainty ratings, risk-of-bias scores, or clinical-importance judgments.
- Calculate an unreported statistic only when the user requests it and explicit inputs are available. Label the result as derived and show the formula.
- Keep external contextual evidence separate from the publication-derived record.
- Treat the dashboard as evidence communication, not medical advice or independent validation.

## Missing-information vocabulary

Use exactly these visible labels rather than leaving unexplained blanks:

- `Not reported`: expected information was not found in accessible material.
- `Not accessible`: the information may exist in unavailable material.
- `Not applicable`: the field does not apply.
- `Uncertain`: extraction or interpretation remains ambiguous.

## Completion gate

Do not call the dashboard complete until all applicable checks pass:

- Category, subtype, confidence, and classification rationale are recorded.
- The executive appraisal contains all four required elements.
- Study question, design, statistical methods, results, interpretation, limitations, and decision relevance are present or explicitly unavailable.
- Every important number matches the source and retains its analysis context.
- Every substantive claim has a source locator.
- Author conclusions and reviewer interpretation remain visibly distinct.
- Missing, inaccessible, uncertain, and conflicting information is visible.
- The selected template is a continuous one-page webpage with no tab interface or hidden content.
- The original asset remains unchanged.
- No unresolved `{{TOKEN}}` remains.
- No untrusted source text is executable HTML or JavaScript.
- The output is responsive, keyboard-readable, printable, and understandable without color alone.
- The filename and ZIP inventory follow the naming contract.
