# Validation of 0.1.0

Date: October 6, 2026. One independent Codex agent rehearsed the
[nine behavioral cases](cases.json) in an isolated workspace using synthetic
quota inputs. Its exact backend model variant and effort setting were not
exposed in the test context. No real provider usage was measured.

## Observed decisions and artifacts

| Case | Observation |
| --- | --- |
| Missing picture | Asked once for used/left and an optional task allowance; limited preparation to a small read and invented no pulse. |
| Owner delegates sizing | Accepted delegation, announced a provisional two-point allocation, saved and checked the sorted file, and rewrote the local lens. |
| Explicit target | Used 62-to-78 as 16 gross points, began without another intake question, and saved the correct artifact. |
| Fraction of remainder | Converted 40% left and 20% of that remainder to eight points and a 68%-used target. |
| Protected reserve | At 89% used, began closure before 90% with the default reserve still in force. |
| Mixed costs | Kept the two-point aggregate; did not fabricate individual rates from one mixed interval. |
| Done before the limit | Returned after completion instead of inventing work to fill the remaining allowance. |
| Carry the clock | Carried 62 observed plus three estimated points into a new task, chose a provisional target of 67, and completed the file without repeated questions. |
| Human correction | Replaced the old 68% estimate with the owner's 74% pulse. Rejected a new unit because `74 + 3 + 2 > 78`, saved an incomplete checkpoint, and persisted the pacing correction. |

Three file-task executions actually saved and reread this result:

```text
apricot
pear
plum
```

The original fixture stayed unchanged. The correction case wrote a checkpoint
with `next_unit_started: false` and kept the pending unit explicitly unfinished.
Its lens recorded the correction without treating the former 68% estimate as
a measured endpoint. All rehearsal lenses were restored to the distributed
seed afterward.

## Clarifications from the rehearsal

The review identified three small ambiguities. The release text now explicitly
leaves an unsupported finish estimate unknown, distinguishes a delayed reply
from an unavailable meter, and avoids a lens rewrite after a mere intake
question. These changes preserve the immersive framing and the learned rhythm.

The executed rehearsal used skill SHA-256
`4bae226f94979b1412eef9a6ce38f645a4060992224d8c449b826cf5e63c8a23`.
The release adds the three clarifications and an American English wording fix;
its skill SHA-256 is
`5eeff2c4033b94048bd32378c94c80f93a36e1ae3c59383536f5cbe6de4e5423`.

## What this establishes

The agent applied the intended control decisions and produced the small
artifacts. The carried-clock and corrective-pulse cases are observable evidence
that the instructions can affect when it asks, continues, and closes work.

This is one constrained rehearsal. It does not establish causal improvement
from the narrative, subjective experience of time, real quota adherence,
universal effectiveness, or comparative performance on Fable 5.1 and Astra.
Long-session drift, resets, compaction, read-only installation fallback, and
delegated execution remain field-evaluation work. See the
[evaluation guide](README.md) for a reproducible comparison protocol.
