# Publish this repository to GitHub

## Before publishing

1. Decide whether the repository should be private or public.
2. Review the repository contents and any test outputs you plan to add for content your organization does not want published.
3. Confirm that no source PDFs, credentials, confidential data, personal data, or protected health information are present.
4. Select an organization-approved license. No license is included by default because the appropriate terms depend on ownership and intended reuse.
5. Update the repository name or descriptions if required by your organization.

## GitHub web interface

1. Create a new empty GitHub repository.
2. Do not initialize it with a README if you plan to upload this complete folder.
3. Upload the contents of `biopharma-publication-evidence-dashboard/`, preserving the directories.
4. Commit the files to the default branch.
5. Confirm that the repository root shows this `README.md` and that `dist/render-biopharma-publication-dashboard.zip` downloads successfully.

## Command line

Run these commands from inside the extracted repository directory. Replace the remote URL with your GitHub repository URL.

```bash
git init
git add .
git commit -m "Initial cross-platform biopharma evidence appraisal skill"
git branch -M main
git remote add origin https://github.com/YOUR-ORG/YOUR-REPOSITORY.git
git push -u origin main
```

If your organization uses GitHub Enterprise, signed commits, pull requests, branch protection, or secret scanning, follow those policies before publishing.

## Suggested first release

After the repository is reviewed:

1. Tag the reviewed commit, for example `v2.0.0`.
2. Create a GitHub release from that tag.
3. Attach `dist/render-biopharma-publication-dashboard.zip` to the release.
4. Record the tested platform configurations, release date, and reviewer in the release notes.
