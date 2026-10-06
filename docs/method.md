# A finite window changes the next decision

Human-facing design notes. Agents only need the installed skill and its
time lens for ordinary operation.

## Origin

On October 6, 2026, Daniil Demidko recorded “Fit and Return” after working with
Fable near the end of a provider's usage window. The initial concern was
interrupted work: partial files, broken references, and conclusions stranded
in the model's context. Budget pulses and coherent units made the work easier
to stop and resume.

The unexpected observation was behavioral: the agent appeared to decide more
quickly and precisely as the visible limit approached. The note described a
single session, including documentation consolidation and several coherent
stops. These are the author's observations, not independently reproduced data.

The concept was first written down in an internal project snippet. The project
was its place of publication, not a dependency of the method. This standalone
edition carries the method and the author's clarifications into a portable
skill; it contains no code from that project.

## Why conviction matters

“Be efficient” leaves the cost of one more branch abstract. A real external
reading makes the tradeoff immediate: the same remaining capacity must fund
discovery, implementation, verification, and the journey back to the user.

The agent-facing premise is direct: **this run ends; bring the work back**.
Its consequence must appear in decisions: price the next complete unit, account
for closure, stop opening optional branches that cannot fit, and preserve the
result. Repeating urgent language without changing those decisions does not
apply the method.

The author's comments call this pressure a “pseudo-fear” of exhaustion. The
protocol gives that intuition an operational form through real limits and
observable commitments. It does not need invented deadlines or a story about
the model's inner experience. This makes the premise usable by both a model
responsive to narrative framing and one that demands explicit accounting.

## The human and agent close different halves of the loop

The owner sees the actual quota interface; the agent sees the work performed
between readings. Where the agent cannot inspect that quota itself, neither
side can calibrate accurately alone. The owner's pulse anchors the estimate.

For every new task, the skill recovers its current time picture. Where that
picture is missing, it invites used/left information and a task allowance.
The owner only has to provide the first; the agent can size the task itself.
A picture grounded in a real pulse and accounted subsequent work remains
useful across task boundaries. A request for another pulse should resolve
decision-relevant uncertainty, not satisfy a ritual.

This distinction is part of the author's subsequent clarification: questions
introduce the human to the concept, then the lens should find the rhythm.
An agent that already knows where it stands should keep working. The protocol
must leave room for that rhythm to emerge through work and corrections.

The owner's corrections are the feedback channel that keeps it real. A new
percentage replaces the agent's extrapolation. A correction about wasted
deliberation, priority, or pacing changes the next decision and the learned
lens. These signals do not require restarting the task. A qualitative pacing
correction does not by itself grant an extra numerical budget.

Use the currently relevant limit, whether a short session window, a weekly
quota, or another displayed boundary. These product details change. “Time” in
the skill's name means the finite opportunity to complete this run; the meter
may measure tokens or usage rather than elapsed minutes.

The author also described the human's satisfaction in reaching a stopping
point and being able to step away. That belongs to the human side of the
method. The agent's objective remains useful, coherent work within the budget.
Filling the meter is not an additional task.

## Calibration must change the method in use

The final comment on the original note expands the idea beyond a one-session
prompt: the installed skill should rewrite itself around its owner's rhythm.
This release implements that through its **time lens**, a file loaded with
the shared protocol and rewritten at the end of governed sessions.

The lens learns more than model prices. It learns the unit size that actually
finished, a closure allowance that proved too small, a reread that changed cost,
and the point at which another branch stopped being worth opening. Rules are
compressed, scoped, and replaced when contradicted. The shared protocol supplies
continuity; the rewritten lens makes future behavior personal.

Per-model cost cannot be inferred from a single mixed-work total. Old rates
cannot silently survive a context or meter change. The original note's sample
rates were observations from one session, so the shipped lens intentionally
starts without numerical prices.

## What success would look like

Measure observable outcomes rather than reported urgency:

- Completed useful units at each interruption or return.
- Coherence of the saved state and the cost of resuming it.
- Actual consumption at closure, including verification and the return.
- Forecast error and the correction carried into the next session.
- Preserved task quality and the amount of unnecessary rework.

Compare similar tasks, model settings, and initial windows with and without the
skill. Repeat runs. Save the external readings alongside the action trace.
Do not count a quicker but incorrect answer as an improvement. See the
[evaluation guide](../evals/README.md) for the release's behavioral cases.

The current claim is a reproducible method and a testable hypothesis. A prompt
cannot enforce a provider's hard cutoff, recover an unsaved result, or prove
equal effectiveness across models merely by sounding certain.
