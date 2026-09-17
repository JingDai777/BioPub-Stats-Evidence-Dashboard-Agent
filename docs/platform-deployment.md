# Platform deployment

The scientific workflow is platform-neutral, but installation and file delivery differ across products. Treat `skill/render-biopharma-publication-dashboard/SKILL.md` and its bundled references, templates, and scripts as the canonical specification. Use `agent/universal-agent-instructions.md` as the persistent agent instruction layer when the platform provides one.

## ChatGPT

ChatGPT supports uploaded skills containing instructions, resources, and code. Upload `dist/render-biopharma-publication-dashboard.zip`, attach or enable the skill for the intended agent or workspace, and use the universal agent instructions.

Official guidance: [Skills in ChatGPT](https://help.openai.com/en-us/articles/20001066-skills-in-chatgpt)

The optional `agents/openai.yaml` file supplies OpenAI-specific display metadata. It does not change the scientific workflow.

## Microsoft Copilot Studio

In the Copilot Studio agent experience that supports skills, upload the same skill ZIP or its `SKILL.md`. Microsoft documents packages containing `SKILL.md` plus optional scripts, templates, and references. Confirm that the chosen agent experience supports file attachments and generated files.

Official guidance: [Add an existing skill to an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-add-existing)

For governed production use, map input retrieval, HTML rendering, storage, and audit retention to approved Copilot tools, flows, connectors, or services. Do not put provider-specific flow calls into the shared `SKILL.md`.

## Claude

Claude custom skills use a directory containing `SKILL.md` plus supporting files and can be uploaded as a ZIP. Claude Managed Agents can also discover skills from `.claude/skills/<skill-name>/` in a mounted repository.

Official guidance: [Skills in Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/skills)

For repository discovery, copy or link the skill source to:

```text
.claude/skills/render-biopharma-publication-dashboard/
```

Keep the relative `assets/`, `references/`, and `scripts/` paths unchanged.

## Gemini

Gemini Gems support persistent instructions and knowledge files, but the consumer Gem workflow does not use this repository's ZIP as a native skill package. Create a Gem, use `agent/universal-agent-instructions.md` as its instructions, and add the relevant Markdown references and HTML templates as knowledge files.

Official guidance: [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780)

If deterministic HTML generation, validation, and ZIP packaging are required, implement those steps through an approved Vertex AI, application, or workflow layer. Preserve the same evidence schema and templates rather than rewriting the scientific logic in platform-specific prompts.

## Cross-platform principle

Maintain one scientific source of truth and adapt only:

- how the publication is supplied;
- how source text is extracted;
- how optional scripts run;
- where files are stored;
- how the HTML, JSON, and ZIP are returned.

Do not create different classification, extraction, or interpretation rules for different model providers.
