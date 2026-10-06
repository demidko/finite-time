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
the agent. Persistence has a concrete artifact: the updated file on disk.

Record the exact skill hash, agent and host identity available to the runner,
messages, actions, output files, and deviations. Reset the seed lens between
unrelated cases; preserve it where a case specifically tests learned rhythm.

These cases check intake, carried time pictures, arithmetic, bounded decisions,
grounded calibration, and adaptation. Synthetic pulses exercise the control
decisions. The field procedure below records actual consumption and completed work.

## Field evaluation

Compare repeated, similar tasks with and without the skill. Keep model, effort,
tools, context regime, initial quota, and acceptance criteria comparable. Have
the human record actual quota readings; the agent cannot supply readings it
does not see. Score completed useful work, correctness, state coherence at
interruption, actual closing cost, and forecast error.

Record each tested model separately, including Fable 5.1 and Astra. Identify
the source of each result: the owner's field record, an executed fixture, or
a measured comparison. Keep unknown readings explicit so the next run can
supply them.

Release-specific observations are recorded in [the validation report](validation-2026-10-06.md).
