# Contributing

Improvements should change a decision the agent makes. Preserve the vivid,
grounded sense of a closing window: it is the method's core, and accounting
supports it. Test framing changes through decisions and results, not by how
urgent the agent says it feels. Keep learned rhythm free from routine questions.

For a field result, include the skill version, exact model or host alias,
reasoning setting, meter kind, initial reading, task allowance, successive
pulses, and the resulting artifacts. Report whether the state was coherent,
what was checked, the actual finishing reading, and what the lens learned.
Distinguish observations from estimates. Remove credentials and private task
contents before sharing a trace.

For a behavior change, run the applicable cases in [evals](evals/README.md)
with an independent agent and describe the outcome. Test Fable 5.1 and Astra
separately when available; a pass on one is not a pass on both. Simulated pulses
test protocol behavior, not cost prediction in a real provider window.

Keep the distributed time lens uncalibrated. Personal rates and preferences
belong in the installed copy. Translate human-facing documentation freely;
keep one canonical agent protocol so fixes do not drift between variants.

Check and package the repository with Python 3.10+:

```sh
python3 scripts/check.py
python3 scripts/package.py
```

The check covers local links, package shape, metadata, and accidental secret
patterns. It does not measure behavioral effectiveness. Release artifacts
contain `SKILL.md`, `TIME-LENS.md`, and the license; repository docs and
evaluation artifacts stay outside the runtime package.
