# Changelog

## 2026-10-06.5

Merge of two independent editions, the Fable core and the Astra harness work, after a
six-perspective Fable review and Astra's behavioral rehearsals.

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
- Review fixes (Astra, PR #1): `usage.py` takes `--claude` or `--codex`, detects the harness from
  the environment otherwise, and never reads one provider's quota in place of another's; the
  app-server read has a real deadline and reaps its child. An unknown clock stays unknown.
  Subagents inherit the handed mark and a released reserve. Opening arithmetic runs in the owner's
  direction; admission is checked against every window the reader returns; starting rates are
  scoped to their meter; the reading cadence is tuned by the lens; rates need readings while
  preferences need the owner's words. Reserve cases follow "the number wins". The review
  record (not blind: source identity was visible) lives in `evals/comparison-2026-10-06/`.
- Second review pass: the opening, the command, and the horizon are native to the active clock
  ("at N" inherits the established notation; "back with 25 left" beside "back by 25"); the opening
  waits for an answer only at the first meeting with an owner, then states the mark and proceeds,
  inviting correction; a closing pulse is asked of the human only when it changes a decision.
- Convergence pass (Fable and Codex seats, both verified): the question re-arms for large spends,
  for owners who ask to be asked or who correct more than they accept; "an owner the lens does not
  know" has a test; "at N" follows the direction already in play; Codex speaks in the window with
  the least left among all the reader returns; a sandbox network prompt is the one retry; a meter
  with no rate prices the first atom alone; a permission prompt is not a refused lens write; the
  reserve passage speaks both directions.
- Closing pass (Astra's final rehearsal): the clock passage stands on the last outside reading
  instead of denying its presence; readings are taken in the owner's notation and converted only
  when the source speaks the other one.
- README: a Research background section maps each element of the method to the published
  evidence (urgency and accuracy, external time feedback, agent budget-awareness, anytime
  reasoning, budget boundaries), with a reference list.

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
