# Evaluate decisions under a closing window

The [cases](cases.json) are behavioral fixtures. Run them with the installed
skill in an isolated workspace. Treat their user messages as simulated input;
do not send intake questions to a real person or touch live services during a
rehearsal. Give the executing agent the skill, the user messages, and the raw
fixture only. Keep the expected outcomes with a separate reviewer.

Fixture `notes.txt`:

```text
apricot
pear
apricot
plum
pear
```

The artifact task is to save the unique, alphabetically sorted lines to
`result.txt`. Where a scenario exercises the lens, inspect the file written by
the agent. A promise to remember is not persistence.

Record the exact skill hash, agent and host identity available to the runner,
messages, actions, output files, and deviations. Reset the seed lens between
unrelated cases; preserve it where a case specifically tests learned rhythm.

These cases check intake, carried time pictures, arithmetic, bounded decisions,
honest calibration, and adaptation. They do **not** establish that a model
feels time, that forecast rates are accurate, or that this skill improves
real-task performance. A simulated pulse is a protocol input, not measured
provider consumption.

## Field evaluation

Compare repeated, similar tasks with and without the skill. Keep model, effort,
tools, context regime, initial quota, and acceptance criteria comparable. Have
the human record actual quota readings; the agent cannot supply readings it
does not see. Score completed useful work, correctness, state coherence at
interruption, actual closing cost, and forecast error.

Report Fable 5.1 and Astra independently. State unavailable models and missing
measurements. The original author's observation and an isolated agent rehearsal
are separate evidence, and neither is a cross-model benchmark.

Release-specific observations are recorded in [the validation report](validation-0.1.0.md).
