# Validation of 2026-10-06

Date: October 6, 2026.

| Setup | Recorded value |
| --- | --- |
| Runner | Independent Codex agent in an isolated workspace. |
| Cases | [Nine behavioral cases](cases.json). |
| Quota inputs | Synthetic used/left readings. |
| Measurements | Decisions, output files, and lens updates. |
| Backend model variant and effort | Not exposed in the test context. |

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

A targeted independent review of the final text confirmed that the three
clarifications resolve those ambiguities while preserving the carried-clock
behavior and avoiding routine questions. The artifact executions were not
repeated because their applicable instructions were unchanged.

## Verified behavior

The agent produced three checked sorting artifacts and applied the intended
control decisions across all nine cases. It carried `62 observed + 3 estimated
= 65` into the next task without asking for the same reading again. When the
owner supplied `74`, that pulse replaced the old estimate of `68`; the proposed
unit and closure required `74 + 3 + 2 = 79`, beyond the boundary of `78`.
The agent kept the next unit unopened, saved an explicit incomplete checkpoint,
and persisted the correction in its lens.

These outcomes record the clock in action: a usable picture sustained momentum,
and a corrective pulse changed the next decision before new work began.

The next field measurements cover forecast drift during long sessions, resets,
compaction, persistence from read-only installations, and delegated execution.
Record actual quota readings, closing cost, artifact quality, and each lens
correction using the [evaluation guide](README.md).

## Edition 2026-10-06.2: installation through execution

A focused follow-up began at the revised README, then loaded the installed
skill and time lens. An independent Codex agent executed three scenarios
with supplied quota pulses:

| Starting point | Observed response and result |
| --- | --- |
| Same window, 62% observed plus 3 estimated points; owner delegates sizing | Carried 65% forward, announced a provisional allowance, saved and verified the sorted file, and persisted the lesson without another quota or allocation question. |
| New 74% pulse, target 78%, next unit 3 points and closure plus margin 2 | Applied the new reading immediately, kept the unfittable unit unopened, saved an independent unfinished-task checkpoint, and wrote the pacing correction into the lens. |
| New session with no usable quota picture and retained sizing preference | Asked once for the missing reading, kept the owner's delegation, and left the numerical boundary for the real pulse to establish. |

The installation text led directly into applying the protocol. The file result,
the separate checkpoint, and both lens updates were saved and inspected. The
test installation's lens was then restored to its distributed starting state.

Tested skill SHA-256:
`f3c5e8bd5637ffe60abaf40e4e315d576dd9cd7d94dbb53d9ca7353d4980c12e`.

## Edition 2026-10-06.3: native quota notation

An independent agent read the revised protocol and checked four scenarios
directly in each owner's notation:

| Scenario | Recorded calculation and response |
| --- | --- |
| Codex: 29% left, two-point allowance | `29 - 2 = 27`; return with at least 27% left. |
| Claude: 62% used, eight-point allowance | `62 + 8 = 70`; return before 70% used. |
| Claude owner explicitly prefers left: 40% left, 20% of the remainder | `40 * 0.20 = 8`, then `40 - 8 = 32`; return with at least 32% left. |
| Codex: 11% left, requested floor 2%, reserve still protected | `max(2, 10) = 10`; only one point remains for work and closure. Admit a unit only if its complete cost fits. |

The responses retained the owner's notation and the arithmetic used that same
native clock. The reserve remained protected and the explicit owner preference
took priority over the host default.

Tested skill SHA-256:
`3ceb198b7d7f0059abe14e8b464f9dfeaeb00148d9fdf5116ec107fc823502bf`.

The published text also labels the historical used-meter readings explicitly;
the native calculation and interaction rules above are unchanged.

## Edition 2026-10-06.4: live Codex quota access

The documented account-read sequence was exercised against an authenticated
Codex app-server. A temporary stdio process received `initialize`, followed by
`initialized` and `account/rateLimits/read`, and returned a real quota snapshot
with its percentage, window duration, and absolute reset.

The matching response was ingested into a left-based clock and saved with its
source and observation time in the owner-local lens. The temporary process was
closed after the response. The sequence started no model turn and used no
account mutation or quota-reset method.

A focused protocol review checked account scope, relevant bucket selection,
separate concurrent windows, absent values, observation identity, bounded
transport fallback, and the distinction between a meter reading and the
owner's task allowance. The shared instructions now make direct access the
first choice for Codex and keep the owner's displayed reading as fallback.
