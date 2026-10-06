# Blind comparison of two finite-time editions, 2026-10-06

Inputs compared, exactly:

| Label shown to judges | Edition | Revision |
| --- | --- | --- |
| Skill A | Fable edition, gitlab.farpost.net/demidko/finite-time | `abc28023b44c232d056870deca3dddd3b1958396` (SKILL.md, calibration.md, usage.py, README.md) |
| Skill B | Astra edition, github.com/demidko/finite-time | `befa4466a5834fc155a591f6819029a951030182` (main as of 09:41 UTC) |

Judges: six fresh contexts of `claude-fable-5-1` at effort `xhigh`, one lens each, run through the
Claude Code Workflow tool. `judges.js` is the exact script, with every prompt verbatim (`COMMON` plus
the six `LENSES`); `judges-output.json` holds each judge's structured output unchanged;
`requirements.md` is the neutral restatement of the owner's instructions the judges read, together
with the owner's note and comments (an internal snippet, not reproduced here). An earlier run of
the same script at effort `max` was stopped before any judge finished; none of its output was used.
The "Fable-seat" and "Codex-seat" lenses are roles the prompt asked the judge to take; the executor
was Claude Fable 5.1 in every run.

Tally: Skill A won the Fable-seat conviction lens (conviction 8 vs 5, immersion 8 vs 4), fidelity
(9 vs 5), operability (6 vs 5), and honesty with the living lens (7 vs 5, 7 vs 6). Skill B won the
Codex-seat lens (universality 8 vs 4) and packaging (7 vs 6).

Limitations a reader should weigh:

- Candidate order was not swapped: A was always the Fable edition and B always the Astra edition.
- All judges are the same model family as the author of Skill A, and the merge plan was written by
  the Fable side from the six reports after the planned merge-architect stage was cancelled for
  budget. Astra's independent behavioral rehearsal in the pull request review is the counterweight.
- The judges rewarded Skill A's experiment framing. The owner later directed that hedging language
  be removed from every artifact an installing agent may read; the merged text follows the owner.
