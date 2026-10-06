# Changelog

## 2026-10-06.5

Merge of two independent editions, the Fable core and the Astra harness work, after a blind
six-lens comparison.

- `SKILL.md`: the protocol-first core from the Fable edition (numbered opening protocol, "back by
  N", starting rates, drift, signal rules, the return, bookends) with the Astra edition's live Codex
  quota read, used/left notation, admission arithmetic, carried time picture, permission boundary,
  and anti-fabrication rules.
- `usage.py`: one reader for both harnesses, Claude Code's OAuth usage endpoint and Codex's
  `account/rateLimits/read` over `codex app-server`. Exit 1 with a reason when no clock can be read.
- `TIME-LENS.md`: neutral seed with sourced starting rates and four blocks: rates, drift, owner,
  decisions.
- Frontmatter carries `metadata.version`, checked against `VERSION`; the package includes `usage.py`.
- README: both self-reads, the always-on line shortened, credits for both editions.

## 2026-10-06.4

- Let Codex retrieve its live ChatGPT quota through the authenticated app-server read method.
- Preserve source, bucket, window, and reset metadata; keep native left reasoning after ingestion.
- Use the owner's displayed reading when direct access is unavailable and retain human control of task budgets and pacing.
- Keep the runtime flat with no additional files or dependencies.

## 2026-10-06.3

- Use left for Codex/ChatGPT and used for Claude by default, with the owner's preference taking priority.
- Reason and communicate in the native meter: subtract spending from left or add it to used, with no routine conversion.
- Document remaining-percentage floors, reserve arithmetic, and examples for both interfaces.

## 2026-10-06.2

Strengthen the installation and activation text around the working record:
Daniil Demidko's Fable field account and independent agent executions.

- Present concrete delivered work, coherent stops, and corrected decisions in the README and skill.
- Carry the immersive time framing through method notes, the personal lens, and release presentation.
- Report protocol checks through their setup and observed outcomes.
- Keep the runtime flat and use a numbered date for another edition on the same day.

## 2026-10-06

Initial release of Finite Time, derived from Daniil Demidko's
“Fit and Return” concept and follow-up clarifications.

- Vivid finite-window framing, with used/left prompts when the current time picture is missing.
- Explicit consumed-point arithmetic, owner reserve, and closure allowance.
- Calibration from external pulses, coherent units, and concise returns.
- Persistent rewriting of the installed time lens, covering rates, decisions, and an emergent owner rhythm.
- Flat Agent Skills package, American English documentation, and behavioral cases.
