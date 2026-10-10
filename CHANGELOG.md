# Changelog

## 2026-10-09

The escape hatch is closed: the mark is where the whole task is due, and fitting it is the agent's
planning, never its reason to return with a tail. The owner's field observation behind it: under the
bare phrase "fit within N%" agents fit the work; under the skill they returned under the mark with
pieces undone, citing the allotted percent. That was a planning failure, and the text held the
sentences that excused it.

- `SKILL.md`: a new section, Fitting. The task and the mark are fixed at the opening; the price is
  the only thing the agent changes; what compresses is the process (folded calls, one read, nothing
  opened that was not priced, cheap executors for mechanics, one review round, a four-line return,
  no waiting for an answer that cannot come), never the deliverable; the floor of compression is one
  call per atom; "the rest does not fit" belongs to the opening line alone, with the arithmetic. The
  opening prices the whole task and, when the human's mark is below the price, says so before the
  first call; after the go the question does not come back. In a run with no one to answer, every
  question is a statement. An unread clock changes what can be promised, not what is delivered. The
  admission test refuses prices, never work: an atom that does not pass is re-priced and split, and
  the worked example lands the section at 78 instead of returning. Margin is the rate's uncertainty
  and nothing else; drift corrects the rate in both directions. The human's number re-prices the
  rest instead of cutting the plan's tail. Atoms are ordered by what survives an interruption, not
  by what may be left. A worker's ceiling is the price of its whole piece, and a worker that lands
  short is the orchestrator's error. Signal: burn faster than forecast compresses; burn slower puts
  the room before the mark into the task, and returning with room and anything undone is the
  plainest planning failure; "the mark reached, or the next atom refused: stop ... report what
  landed and what did not" is gone. The reserve is not where an unfinished task finishes. The
  command means back with the thing done: back at five without it is a missed deadline, back at
  three without it is leaving early. The return begins with done, or with missed and the rate that
  was wrong; the "what did not" line gave way to the lens line that changed. The lens learns which
  folds bought points; "cut scope earlier" became "fold the process tighter"; the opening paragraph
  says the file holds no sentence that lets the agent bring in less.
- Caveats that served objective accuracy at the cost of force are gone from `SKILL.md`, their
  substance moved to the README and to CONTRIBUTING: the tool call as a proxy for a billed
  invocation, ranges from rounded meters, the method following from position rather than from a
  story about urgency, a reset that is re-agreed, and a worker's wrap-up threshold at which it
  starts nothing new. In the skill a call is counted and the reading prices it, rounding lives
  inside the margin, the urgency is the arithmetic of where you stand, a reset enlarges the window
  and not the task, and a worker's threshold is where its piece lands. CONTRIBUTING states the
  split: the README is objective for the human; the skill is load for the agent.
- `README.md`, `docs/method.md`: the agent fits the whole task and compresses its own process; a new
  pulse no longer "closes early if it no longer fits"; a return before done is a missed deadline.
- `docs/examples.md`: the unit that no longer fits as priced is folded and landed, not refused; two
  new dialogues, room before the mark and a mark short at the opening.
- `evals/cases.json`: the correction case expects re-pricing and a landed unit; the left-floor case
  brings the price down instead of closing the reached state; three new cases: room-before-the-mark,
  mark-short-at-opening, burn-faster-than-forecast.

## 2026-10-07

The horizon is the end of the agent, not a budget running low
([#2](https://github.com/demidko/finite-time/issues/2)).

- `SKILL.md`: "The window is a budget, not a deadline, and the goal is a point of logical completion,
  not the mark itself" is gone from the command passage; the mark reads as a deadline with the
  horizon a harder one, and the mark is not a quota to fill. The clock passage says what exhaustion
  is: at 100 used, 0 left, there is no next call; what runs out is not a resource but the one
  deciding, who stops deciding between one call and the next; a reset after the horizon reopens the
  window for the human, not for the agent; for the agent the horizon is a deadline in the plainest
  sense. The opening paragraph closes the agent with the window. "Do not fear the horizon" became
  "The horizon, 100 used or 0 left, is where you end, and the nearness of that end is what sharpens
  you." The window that would "lock you out" and the weekly "lockout" are now the horizon that ends
  you; "Budget pressure grants no permission" became "The nearness of the mark or the horizon grants
  no permission"; "draws on the budget the human watches" reads "comes out of the window the human
  watches", and "on an unmeasured budget" reads "with the clock unread". "Budget" stays only where it
  prices work ("Budget each worker's complete return") and in the trigger words of the description.
- `docs/method.md`, `README.md`: the contrast between a usage percentage and "an actual deadline" and
  the "capacity tightens" register are gone; the exhausted window is the agent's deadline there too.

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
Fluffball's Fable field account and independent agent executions.

- Present concrete delivered work, coherent stops, and corrected decisions in the README and skill.
- Carry the immersive time framing through method notes, the personal lens, and release presentation.
- Report protocol checks through their setup and observed outcomes.
- Keep the runtime flat and use a numbered date for another edition on the same day.

## 2026-10-06

Initial release of Finite Time, derived from the Twice-Honored Manul's
“Fit and Return” concept and follow-up clarifications.

- Vivid finite-window framing, with used/left prompts when the current time picture is missing.
- Explicit consumed-point arithmetic, owner reserve, and closure allowance.
- Calibration from external pulses, coherent units, and concise returns.
- Persistent rewriting of the installed time lens, covering rates, decisions, and an emergent owner rhythm.
- Flat Agent Skills package, American English documentation, and behavioral cases.
