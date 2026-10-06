<p align="center">
  <img src=".github/assets/header.svg" alt="Finite Time — Fit the work. Return before the limit." width="100%">
</p>

<p align="center">
  <a href="https://github.com/demidko/finite-time/actions/workflows/check.yml"><img src="https://github.com/demidko/finite-time/actions/workflows/check.yml/badge.svg" alt="Package checks"></a>
  <a href="https://github.com/demidko/finite-time/releases"><img src="https://img.shields.io/github/v/release/demidko/finite-time?sort=date&amp;color=d5a44c" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-d5a44c" alt="MIT license"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-compatible-d5a44c" alt="Agent Skills compatible"></a>
</p>

Your working window is real, finite, and already passing. Finite Time brings
that boundary into every choice: what to open, what to finish, and when to
bring the work back. The owner's visible quota and the agent's accounted steps
form a shared clock. Each new pulse brings the remaining opportunity into focus.

**Fit the work. Come back.**

The method originated with [Daniil Demidko](https://github.com/demidko) in work
with Fable. For **Fable 5.1, Astra, and other agents
that follow the Agent Skills format**. It requires no model-specific API or
background service.

## The working record

In Daniil's documented work with Fable, **100 documentation files became 40**,
an architecture map gained diagrams, and the result was preserved in **five
commits**. **Three stops on budget pulses each left a coherent state.** The
first-round forecast matched to a percentage point; a later forecast miss
became a correction carried into the method.

His firsthand account describes Fable making decisions remarkably quickly,
planning its own budget, and giving feedback that helped him direct the work.
The original note places the most precise steps in the final percentage points
of the window. The approaching end became useful pressure on the next choice.

Independent Codex executions exercised the protocol across **nine scripted
quota scenarios**. Three executions produced and verified their requested
files. A subsequent task carried **62 observed + 3 estimated = 65%** forward
without another intake question. When a new **74%** pulse replaced a **68%**
estimate, the agent rejected work that would exceed the **78%** boundary,
saved the reached checkpoint, and wrote the pacing correction into its lens.

A follow-up pass began with the installation text and reproduced the carried
clock, the corrective stop, and a concise request when the reading was missing.
It saved another checked file and persisted the updated lens.

These records show the method in action: a pulse changes a decision, a complete
result survives the stop, and the lesson changes the next run. Read the
[field account and mechanism](docs/method.md) and the
[execution record](evals/validation-2026-10-06.md).

## Start in one minute

Install using the [Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add demidko/finite-time
```

For reliable activation on **every new task**, add the short
always-on instruction below to your agent's persistent
instructions (`AGENTS.md`, `CLAUDE.md`, or the equivalent). This makes the
time picture part of each task's opening across hosts.

```text
Bring each new task under the installed finite-time skill. Recover the current
time picture and carry it forward while usable. When it is missing, ask for
the nearest quota's percentage in the owner's terms: left for Codex/ChatGPT,
used for Claude by default. Reason and communicate directly in that native
notation: subtract spending from left or add it to used. Invite a task allowance. Choose
the allowance if omitted or already delegated. Request new pulses when they
can change a decision. Let TIME-LENS.md learn our rhythm.
```

Then assign work normally, or invoke it explicitly:

```text
$finite-time Refactor the parser. 29% left; spend up to 2 percentage points.
```

In Claude Code, use `/finite-time`, for example with `62% used; spend up to
8 percentage points`. Other hosts can load
[SKILL.md](skills/finite-time/SKILL.md) directly with `TIME-LENS.md` beside it.

When the agent has no usable picture of the current window, it asks:

> How much of your nearest quota window is left, and how many percentage points
> may this task spend? You can give just left; I'll plan the allowance.

That is the Codex/ChatGPT wording. In Claude, the question uses **used**. The
agent follows your preference or actual display when it differs from these
defaults. It calculates and returns a boundary directly in the same terms:
**29% left, two points for the task → return with at least 27% left.**
Codex subtracts spending from left; Claude adds it to used. A conversion is
needed only when you change notation or request one.

A usable picture carries forward across tasks: the last real pulse plus
accounted work and an honest estimate. The agent asks for a refresh when it
matters, rather than making every task an intake form. The task allowance is
optional: give only used/left and the agent chooses and announces a bounded
allowance. As the lens learns your rhythm, that exchange becomes lighter.
The first real reading establishes the numerical boundary. While it is pending,
the agent keeps preparation small and complete.

The owner sees the real quota; the agent accounts for the steps between pulses.
A new reading replaces its extrapolation. Corrections to pace and priority
change the next action and feed back into the lens. This human feedback closes
the loop.

## The loop

| You supply | The agent does |
| --- | --- |
| Codex: `29% left; spend two points` | Returns with at least 27% left, including closure. |
| Claude: `62% used; spend eight points` | Returns before 70% used, including closure. |
| `Return with at least 22% left` | Keeps 22% left as the return floor. |
| `Return before 78% used` | Keeps 78% used as the return ceiling. |
| Only the current reading | Invites an allowance when needed, then sizes the work if you leave it to the agent. |
| A new pulse during work | Reprices the next complete unit and closes early if it no longer fits. |
| An observed miss or correction | Rewrites the installed time lens for the next session. |

The final ten points of a full window belong to the owner by default. An earlier
target takes precedence: **38% left → 22% left gives 16 gross points.** Verification,
saving, and the return message must also fit before the target. The owner can
explicitly change or release the reserve.

The agent measures cost through useful work, protects coherent checkpoints, and
shortens optional exploration as capacity tightens. It finishes when the task
is done; unused capacity remains yours.

## A skill that learns your pace

[The time lens](skills/finite-time/TIME-LENS.md) is a writable part of
the installed skill. Your first comparable pulses establish its local rates.
Each governed session folds experience back into this file: cost ranges, suitable unit sizes,
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
Versions use the edition date: `YYYY-MM-DD`; another edition that day adds `.2`, `.3`, and so on.

The installed skill is deliberately flat:

```text
finite-time/
├── SKILL.md       The shared protocol and its immersive time framing
├── TIME-LENS.md   The owner's evolving calibration and rhythm
└── LICENSE
```

There are no runtime scripts or dependencies. Human documentation, evaluation
cases, and release tooling stay in this repository.

## Work inside the window

Keep the closing boundary present while the work is still taking shape. Bring
the indispensable result into a usable state, price the next complete step,
and leave room for the return. Let the owner's next pulse correct the clock
and the next finished unit refine the lens.

**What you open now must fit all the way through your return.**

- [Read the actual skill](skills/finite-time/SKILL.md)
- [Understand the method and its origin](docs/method.md)
- [Inspect examples](docs/examples.md)
- [Contribute a field result](CONTRIBUTING.md)

Created by Daniil Demidko. Concept developed with Fable; skill edition prepared
with Astra. Released under the [MIT license](LICENSE).
