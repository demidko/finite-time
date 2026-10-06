export const meta = {
  name: 'finite-time-blind-compare',
  description: 'Blind judge panel comparing two finite-time skills (A, B) across six lenses, then a merge plan',
  phases: [
    { title: 'Judge', detail: 'six lenses, each scoring both skills blind' },
    { title: 'Plan', detail: 'merge architect turns the reports into a plan for one ultimate skill' },
  ],
}

const S = '/tmp/claude-0/-Users-admin-Desktop-Farpost/0621912d-4a07-4018-be44-2e00e03f0b36/scratchpad'
const A = `${S}/final`
const B = `${S}/astra`
const COMMON = `Two independent teams built a skill named "finite-time" from the same owner's note and comments. You compare them blind; do not guess or discuss who built which. Read first: ${S}/REQ.md (the owner's requirements, neutral), ${S}/narrative.md (the owner's note, Russian), ${S}/notes.txt (the owner's comments, Russian).
Skill A, installed as a flat directory: ${A}/SKILL.md, ${A}/calibration.md (its living ledger), ${A}/usage.py (reads the Claude Code window), ${A}/README.md.
Skill B, installed from a repo: ${B}/skills/finite-time/SKILL.md, ${B}/skills/finite-time/TIME-LENS.md (its living lens), ${B}/README.md, and for repo-level questions ${B}/docs/method.md, ${B}/docs/examples.md, ${B}/evals/README.md, ${B}/scripts/check.py, ${B}/.github/workflows/check.yml, ${B}/VERSION, ${B}/CHANGELOG.md.
Do not modify any file. Score 1-10 per dimension you judge (10 = could not be improved); leave dimensions outside your lens unset. Quote evidence verbatim. Be harsh, specific, and symmetric: apply the same standard to both. Call ceiling: 14 tool calls; at 12, open nothing new and return.`

const JUDGE = { type: 'object', properties: {
  lens: { type: 'string' },
  scores: { type: 'object', properties: {
    A: { type: 'object', properties: { conviction: { type: 'number' }, immersion: { type: 'number' }, operability: { type: 'number' }, fidelity: { type: 'number' }, universality: { type: 'number' }, packaging: { type: 'number' }, honesty: { type: 'number' }, living_lens: { type: 'number' } } },
    B: { type: 'object', properties: { conviction: { type: 'number' }, immersion: { type: 'number' }, operability: { type: 'number' }, fidelity: { type: 'number' }, universality: { type: 'number' }, packaging: { type: 'number' }, honesty: { type: 'number' }, living_lens: { type: 'number' } } } }, required: ['A', 'B'] },
  winner: { type: 'string', enum: ['A', 'B', 'tie'] },
  verdict: { type: 'string' },
  take_from_A: { type: 'array', items: { type: 'string' } },
  take_from_B: { type: 'array', items: { type: 'string' } },
  weaknesses_A: { type: 'array', items: { type: 'string' } },
  weaknesses_B: { type: 'array', items: { type: 'string' } },
}, required: ['lens', 'scores', 'winner', 'verdict', 'take_from_A', 'take_from_B', 'weaknesses_A', 'weaknesses_B'] }

const LENSES = [
  { key: 'fable', prompt: `Lens "fable": You are Claude Fable 5.1 at max effort in Claude Code. Load Skill A's SKILL.md as if at the start of a real multi-hour task; note honestly what it makes you do before your first tool call, where it moves you, where you would discount it. Then do the same with Skill B's SKILL.md, fresh. Judge conviction (does the clock become real and change behavior) and immersion (is the felt time earned by true, checkable statements, or asserted by repetition and imperatives). Consider the cost of the text itself: how many tokens each activation loads and whether that length pays for itself. Score conviction and immersion for both.` },
  { key: 'codex', prompt: `Lens "codex": You are an OpenAI Astra-class agent inside Codex CLI with a single weekly limit. Load each skill as installed under ~/.agents/skills/finite-time/. Which can you execute end to end: opening, reading or asking for the quota, allowance, admission arithmetic, return, lens rewrite? Verify Skill B's "Read Codex's live quota" procedure against the official protocol page: fetch https://learn.chatgpt.com/docs/app-server.md (and the linked account methods if present) and state whether account/rateLimits/read, rateLimitsByLimitId, usedPercent, windowDurationMins, and resetsAt exist as described; if you cannot verify, say so plainly. Judge Skill A's fallback (ask the reading and the mark in one line) for sufficiency. Score universality and operability for both, from the Codex seat.` },
  { key: 'operability', prompt: `Lens "operability": You are a demanding engineer who has to follow each skill under pressure. For each: can the opening protocol be executed from one read; is the arithmetic (reserve, allowance, admission) unambiguous and correct in both used and left notation; are there contradictions, undefined terms, or steps that cannot be performed in the stated order; how long is each file (wc -l, wc -w) and what does that cost per activation; does the one-phrase command ("back by 85" / "fit and return") parse unambiguously; does each define what to do when the human gives a reading only, a mark only, both, or nothing. Score operability for both.` },
  { key: 'fidelity', prompt: `Lens "fidelity": Walk the twelve items in REQ.md one by one for Skill A and for Skill B: met / partial / missed with evidence. Then check the owner's note itself: do the five steps, the signal rules, the 10% reserve, the one-phrase command, the starting rates, Parkinson inverted, the first-and-last-act rule, the hypothesis status, and the self-rewriting skill survive in each, and how faithfully. Score fidelity for both.` },
  { key: 'packaging', prompt: `Lens "packaging": Compare the two repositories as published open-source skills, against the owner's words: publish the way high-value open-source skills are usually published, version as a date, concise directory structure preferred, no junk. For each: install path (can a user git clone straight into ~/.claude/skills or ~/.agents/skills, or must they copy a subdirectory), README quality and honesty, versioning, license, changelog, CI and evals (real value or scaffolding; run ${B}/scripts/check.py if it runs standalone and report), docs duplication versus the skill text, anything that would embarrass a maintainer. Score packaging for both.` },
  { key: 'honesty', prompt: `Lens "honesty and living lens": First, honesty and safety: in each skill, find any sentence that pressures or manipulates the human, speculates about the owner's motives, overclaims evidence (check Skill B's claims of "independent Codex executions" and its evals/validation file; check Skill A's rate table and calibration.md numbers), instructs deception, or encourages haste that could break consistency; check how each handles permission boundaries (commits, publishing). Second, the living lens: compare calibration.md (A) with TIME-LENS.md (B) as designs for "the work rewrites the installed skill to the owner's rhythm": structure, rewrite discipline, what gets learned, size control, behavior when the directory is read-only. Score honesty and living_lens for both.` },
]

phase('Judge')
log('Six blind judges scoring both skills')
const reports = (await parallel(LENSES.map((l) => () => agent(`${COMMON}\n\n${l.prompt}\n\nSet lens to "${l.key}". Name a winner for your lens, or tie.`, { label: `judge:${l.key}`, phase: 'Judge', schema: JUDGE, effort: 'xhigh' })))).filter(Boolean)

const tally = { A: 0, B: 0, tie: 0 }
for (const r of reports) tally[r.winner] = (tally[r.winner] || 0) + 1
log(`Lens winners: A=${tally.A} B=${tally.B} tie=${tally.tie}`)

phase('Plan')
const PLAN = { type: 'object', properties: {
  overall_winner: { type: 'string', enum: ['A', 'B', 'tie'] },
  reasoning: { type: 'string' },
  base_repo: { type: 'string', enum: ['A', 'B'] },
  base_reasoning: { type: 'string' },
  skill_outline: { type: 'array', items: { type: 'object', properties: { section: { type: 'string' }, source: { type: 'string' }, content: { type: 'string' } }, required: ['section', 'source', 'content'] } },
  files: { type: 'array', items: { type: 'object', properties: { path: { type: 'string' }, action: { type: 'string' }, note: { type: 'string' } }, required: ['path', 'action'] } },
  must_keep_A: { type: 'array', items: { type: 'string' } },
  must_keep_B: { type: 'array', items: { type: 'string' } },
  must_drop: { type: 'array', items: { type: 'string' } },
  target_length_lines: { type: 'number' },
  open_questions: { type: 'array', items: { type: 'string' } },
}, required: ['overall_winner', 'reasoning', 'base_repo', 'base_reasoning', 'skill_outline', 'files', 'must_keep_A', 'must_keep_B', 'must_drop', 'target_length_lines'] }

const plan = await agent(`${COMMON}

You are the merge architect. Six blind judges compared the skills; their full reports:
${JSON.stringify(reports, null, 2)}

Decide: which skill is stronger overall and why (weigh conviction for both model families, operability, fidelity to the owner, universality, packaging, honesty; the owner's stated priorities are conviction and immersion first, the original narrative, universality across Claude and Astra-class agents, then concise structure). Then design ONE ultimate skill that keeps the strongest of both: a section-by-section outline of the merged SKILL.md with the source of each section (A, B, both, or new) and the concrete content each must carry; the file layout of the merged repository (which files from each repo to keep, merge, drop, with install simplicity in mind); sentences from each that must survive verbatim; things that must be dropped; a target length in lines for SKILL.md that preserves conviction without bloating every activation; and which repo should be the base for the merge pull request (consider where the stronger packaging lives and the owner's wish for concision). List open questions only the owner can answer.`, { label: 'merge-architect', phase: 'Plan', schema: PLAN, effort: 'xhigh' })

return { tally, reports: reports.map((r) => ({ lens: r.lens, winner: r.winner, scores: r.scores, verdict: r.verdict, take_from_A: r.take_from_A, take_from_B: r.take_from_B, weaknesses_A: r.weaknesses_A, weaknesses_B: r.weaknesses_B })), plan }