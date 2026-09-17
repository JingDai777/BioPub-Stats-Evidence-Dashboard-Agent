# Biopharma Publication Evidence Dashboard

A cross-platform agent skill that converts one biomedical or biopharma publication into a source-traceable, continuous HTML evidence appraisal.

The project is designed from an industry biostatistics perspective. It goes beyond article summarization by making the statistical methodology, effect estimates, uncertainty, robustness, interpretation, limitations, and decision relevance visible in one top-to-bottom report.

Developed by **Jing Dai, PhD**.

## What the agent produces

For each publication, the workflow creates:

- a standalone HTML evidence dashboard;
- a structured JSON evidence record;
- a ZIP that preserves both filenames.

Every dashboard begins with four elements:

1. **Reported finding**
2. **Biostatistical interpretation**
3. **Primary limitation**
4. **Decision relevance**

The detailed report then proceeds continuously through the research question, design, statistical methods, results, interpretation, limitations, transparency, extraction notes, and source map. The templates use no tabs, accordions, hidden panels, or external runtime dependencies.

## Supported publication categories

| Category | Statistical focus | Template |
| --- | --- | --- |
| Clinical Trial | Estimand, endpoints, analysis populations, model, multiplicity, missing data, sensitivity analyses, efficacy and safety | `clinical-trial-dashboard.html` |
| Observational Study | Target contrast, cohort construction, confounding control, matching or weighting, diagnostics, bias and causal caution | `observational-study-dashboard.html` |
| Systematic Review/Meta-analysis | Effect-measure harmonization, synthesis estimator, heterogeneity, prediction intervals, risk of bias and certainty | `systematic-review-dashboard.html` |
| Other Publication | Subtype-specific appraisal for biomarkers, prediction models, guidelines, economic models, PK/PD, protocols and other evidence | `other-publication-dashboard.html` |

## Repository structure

```text
biopharma-publication-evidence-dashboard/
├── README.md
├── agent/
│   ├── universal-agent-instructions.md
│   └── starter-prompts.md
├── docs/
│   ├── platform-deployment.md
│   ├── skill-packaging.md
│   ├── validation-and-governance.md
│   └── github-publishing.md
├── skill/
│   └── render-biopharma-publication-dashboard/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       ├── references/
│       └── scripts/
└── dist/
    └── render-biopharma-publication-dashboard.zip
```

`skill/render-biopharma-publication-dashboard/` is the canonical skill source. The `dist/` ZIP is a generated distribution artifact.

## Platform use

The `SKILL.md` is written without provider-specific tool names or storage assumptions. Installation still differs by platform:

- **ChatGPT:** upload the skill ZIP and use the universal agent instructions. See [Skills in ChatGPT](https://help.openai.com/en-us/articles/20001066-skills-in-chatgpt).
- **Microsoft Copilot Studio:** upload `SKILL.md` or the skill ZIP in a supported agent experience. See [Add an existing skill to an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-add-existing).
- **Claude:** upload the custom skill ZIP or expose the skill under `.claude/skills/` in a supported repository-backed agent. See [Skills in Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/skills).
- **Gemini:** use the universal agent instructions and add the relevant references and templates as Gem knowledge files. Gemini Gems do not use this ZIP as a native skill package. See [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780).

Read [platform deployment](docs/platform-deployment.md) before configuring a production agent.

## Quick start

1. Download and extract this repository.
2. Use `dist/render-biopharma-publication-dashboard.zip` where the platform supports skill upload.
3. Use `agent/universal-agent-instructions.md` as the agent's persistent instructions when the platform provides that field.
4. Enable the approved capabilities required to read publications and create HTML, JSON, and ZIP files.
5. Test at least one approved publication from each category before broader use.

Example request:

> Create a source-traceable biostatistical evidence appraisal from this publication. Emphasize the statistical methodology, interpretation, limitations, and decision relevance. Return the continuous HTML dashboard, evidence JSON, and filename-preserving ZIP.

## Output contract

```text
<first-author-surname>-<publication-year>-publication-dashboard.html
<first-author-surname>-<publication-year>-evidence.json
<first-author-surname>-<publication-year>-publication-dashboard.zip
```

The ZIP contains the HTML and evidence JSON at the archive root. This preserves the intended filename when a chat interface renames a directly previewed HTML file.

## Local validation

From the repository root:

```bash
python3 skill/render-biopharma-publication-dashboard/scripts/validate_dashboard.py --self-test
python3 -m py_compile \
  skill/render-biopharma-publication-dashboard/scripts/validate_dashboard.py \
  skill/render-biopharma-publication-dashboard/scripts/package_dashboard.py
```

For a completed dashboard:

```bash
python3 skill/render-biopharma-publication-dashboard/scripts/validate_dashboard.py \
  --evidence path/to/evidence.json \
  --html path/to/publication-dashboard.html
```

Validator success confirms structural requirements. It does not prove scientific accuracy or suitability for a clinical, regulatory, commercial, or investment decision.

## Scientific safeguards

- Every material method, result, limitation, funding statement, and conflict statement must have a source locator.
- Reported findings, author conclusions, author limitations, reviewer interpretation, and derived calculations remain distinct.
- Missing information is labeled rather than inferred.
- Observational associations are not converted into causal claims.
- Exploratory, subgroup, pooled, and post hoc findings are not presented as prespecified primary evidence.
- Statistical significance is interpreted with effect magnitude, precision, robustness, and clinical context.

See [validation and governance](docs/validation-and-governance.md) for the recommended review and release controls.

## Intended use

This project supports evidence communication and methodological appraisal. It is not medical advice, a clinical decision-support system, a regulatory assessment, or a substitute for independent review of the original publication.

## Publishing and license

Before making the repository public, remove confidential or licensed source material, review generated examples, and add an ownership-appropriate license. No license is included by default.

See [GitHub publishing](docs/github-publishing.md).
