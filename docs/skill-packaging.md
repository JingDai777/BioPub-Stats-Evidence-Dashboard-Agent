# Skill packaging

## Source of truth

Edit only:

```text
skill/render-biopharma-publication-dashboard/
```

The ZIP under `dist/` is generated output. Rebuild it after changing the skill, references, templates, or scripts.

## Relative paths

The directory containing `SKILL.md` is the skill root. All references use paths relative to that directory. No file needs an absolute path to a computer, workspace, or storage service.

## Build the distribution ZIP

From the repository root:

```bash
cd skill/render-biopharma-publication-dashboard
zip -r ../../dist/render-biopharma-publication-dashboard.zip \
  SKILL.md agents assets references scripts \
  -x '*/__pycache__/*' '*.pyc' '.DS_Store'
cd ../..
```

The archive must open directly to `SKILL.md`, `agents/`, `assets/`, `references/`, and `scripts/`. Do not add an extra wrapper directory.

## Validate before release

```bash
python3 skill/render-biopharma-publication-dashboard/scripts/validate_dashboard.py --self-test
python3 -m py_compile \
  skill/render-biopharma-publication-dashboard/scripts/validate_dashboard.py \
  skill/render-biopharma-publication-dashboard/scripts/package_dashboard.py
unzip -l dist/render-biopharma-publication-dashboard.zip
```

Also confirm that:

- exactly four HTML templates exist;
- every template contains the four-part executive appraisal;
- every template uses sequential `.report-section` elements;
- no template contains a tab role, `<details>`, or unresolved non-template scaffolding;
- the templates contain no external script or stylesheet dependency.
