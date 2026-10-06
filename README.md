<p align="center">
  <img src=".github/assets/header.svg" alt="Finite Time — Fit the work. Return before the limit." width="100%">
</p>

<p align="center">
  <a href="https://github.com/demidko/finite-time/actions/workflows/check.yml"><img src="https://github.com/demidko/finite-time/actions/workflows/check.yml/badge.svg" alt="Package checks"></a>
  <a href="https://github.com/demidko/finite-time/releases"><img src="https://img.shields.io/github/v/release/demidko/finite-time?sort=date&amp;color=d5a44c" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-d5a44c" alt="MIT license"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-compatible-d5a44c" alt="Agent Skills compatible"></a>
</p>

An agent skill that makes the end of a working window part of every decision.
Give the agent your real quota reading. It budgets the task, makes complete
steps, and brings the work back before the boundary.

**Fit the work. Come back.**

The method originated with [Daniil Demidko](https://github.com/demidko) in work
with Fable. This edition is designed for **Fable 5.1, Astra, and other agents
that follow the Agent Skills format**. It requires no model-specific API or
background service.

## Start in one minute

Install using the [Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add demidko/finite-time
```

For reliable activation on **every new task**, add the short
always-on instruction below to your agent's persistent
instructions (`AGENTS.md`, `CLAUDE.md`, or the equivalent). A skill's discovery
description alone cannot guarantee that every host loads it on every turn.

```text
Bring each new task under the installed finite-time skill. Recover the current
time picture and carry it forward while usable. When it is missing, ask for
the nearest quota's used/left percentage and invite a task allowance. Choose
the allowance if omitted or already delegated. Request new pulses when they
can change a decision. Let TIME-LENS.md learn our rhythm.
```

Then assign work normally, or invoke it explicitly:

```text
$finite-time Refactor the parser. 62% used; spend up to 8 percentage points.
```

In Claude Code, use `/finite-time`. Other hosts can load
[SKILL.md](skills/finite-time/SKILL.md) directly with `TIME-LENS.md` beside it.

When the agent has no usable picture of the current window, it asks:

> How much of your nearest quota window is used or left, and how many percentage
> points may this task spend? You can give just used/left; I'll plan the task
> allowance.

A usable picture carries forward across tasks: the last real pulse plus
accounted work and an honest estimate. The agent asks for a refresh when it
matters, rather than making every task an intake form. The task allowance is
optional: give only used/left and the agent chooses and announces a bounded
allowance. As the lens learns your rhythm, that exchange becomes lighter.
Without a real reading, the agent can do small complete units but cannot
promise a numerical finishing percentage.

The owner sees the real quota; the agent accounts for the steps between pulses.
A new reading replaces its extrapolation. Corrections to pace and priority
change the next action and feed back into the lens. This human feedback closes
the loop.

## The loop

| You supply | The agent does |
| --- | --- |
| A real reading: `62% used` or `38% left` | Establishes the same 38-point remainder. |
| `Spend 8% on this task` | Plans to return by 70% used, including closure. |
| `Return by 78%` | Treats 78% as an absolute boundary. |
| Only the current reading | Invites an allowance when needed, then sizes the work if you leave it to the agent. |
| A new pulse during work | Reprices the next complete unit and closes early if it no longer fits. |
| An observed miss or correction | Rewrites the installed time lens for the next session. |

The final ten points of a full window belong to the owner by default. An earlier
target takes precedence: **62 → 78 means 16 gross points, not six.** Verification,
saving, and the return message must also fit before the target. The owner can
explicitly change or release the reserve.

The agent measures cost through useful work, protects coherent checkpoints, and
shortens optional exploration as capacity tightens. It finishes when the task
is done; unused capacity remains yours.

## A skill that learns your pace

[The time lens](skills/finite-time/TIME-LENS.md) is a writable part of
the installed skill. It starts without invented measurements. Each governed
session folds evidence back into this file: cost ranges, suitable unit sizes,
closure overhead, decision habits, and your preferred rhythm.

The agent **rewrites** compact rules instead of appending a diary. The shared
protocol stays stable while its personal application changes. A model switch
or a new window makes old rates provisional. A read-only host can use persistent
owner-local memory or return a lens patch for manual saving.

Back up your personalized lens before reinstalling or updating. Restore it over
the new seed afterward. Keep personal observations out of upstream pull requests.

## Manual installation

First installation:

```sh
git clone https://github.com/demidko/finite-time.git
mkdir -p ~/.agents/skills
cp -R finite-time/skills/finite-time ~/.agents/skills/finite-time
```

For Claude Code, use `~/.claude/skills` instead. A project-local copy can go in
`.agents/skills` or `.claude/skills`. Use one discovery path per host to avoid
duplicate entries. Then add the always-on instruction above.

These locations follow the official [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
and [Claude Code skill documentation](https://code.claude.com/docs/en/skills).
An installable ZIP is also attached to each [release](https://github.com/demidko/finite-time/releases).
Versions use the edition date: `YYYY-MM-DD`.

The installed skill is deliberately flat:

```text
finite-time/
├── SKILL.md       The shared protocol and its immersive time framing
├── TIME-LENS.md   The owner's evolving calibration and rhythm
└── LICENSE
```

There are no runtime scripts or dependencies. Human documentation, evaluation
cases, and release tooling stay in this repository.

## What is established

The original observation came from one working session. The author reported
faster decisions near the limit and coherent results across several stops.
That motivated the method; it does not establish a universal performance gain.

This release provides a portable protocol, a personal learning mechanism, and
[reproducible behavioral cases](evals/README.md). Fable 5.1 and Astra are design
targets, not a claim of a completed comparative benchmark. The skill guides
behavior; it cannot enforce a provider's quota or prevent an abrupt termination.

- [Read the actual skill](skills/finite-time/SKILL.md)
- [Understand the method and its origin](docs/method.md)
- [Inspect examples](docs/examples.md)
- [Contribute a field result](CONTRIBUTING.md)

Created by Daniil Demidko. Concept developed with Fable; skill edition prepared
with Astra. Released under the [MIT license](LICENSE).
