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
bring the work back. The real quota and the agent's accounted steps form a
shared clock. The agent reads its live meter itself, in Claude Code and in Codex; otherwise the
owner supplies the displayed number. Each pulse brings the remainder into focus.

**Fit the work. Back by 85.** One phrase steers the whole method: the agent reads the clock,
lands every unit of work in a committed state, and returns at or before the percent you named.

The method originated with [Daniil Demidko](https://github.com/demidko) in work
with Fable. For **Fable 5.1, Astra, and other agents
that follow the Agent Skills format**. It ships one standard-library reader script and
needs no background service.

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
files. A subsequent task carried **62% used + 3 estimated points = 65% used**
forward without another intake question. When a new **74% used** pulse replaced
a **68% used** estimate, the agent rejected work that would exceed **78% used**,
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
Before any task, follow the finite-time skill: read the clock with its usage.py, agree on the
mark in one line, work in atoms, land, return. Let TIME-LENS.md learn our rhythm.
```

Then say what you want and when you want it back:

```text
Move the auth tests to the new fixture. Back by 85.
```

The agent reads the clock itself, prices the work, works in atoms, and returns at or before 85%
of your window with four lines: what landed, what did not, the percent it landed at, and the next
step as a choice. Give no mark and it proposes one in a single line; "ok" is enough. Correct the
clock whenever you like ("you're at 62", "make it 80 instead"); your number always wins.

In Codex the same phrase reads in left terms, or invoke the skill explicitly:

```text
$finite-time Refactor the parser. 29% left; spend up to 2 percentage points.
```

In Claude Code, use `/finite-time`, for example with `62% used; spend up to
8 percentage points`. Other hosts can load
[SKILL.md](skills/finite-time/SKILL.md) directly with `TIME-LENS.md` beside it.

When the agent needs a quota pulse it runs `usage.py`. In Claude Code the script reads the
harness's own OAuth login for the 5-hour and 7-day windows; in Codex it reads the authenticated
app-server meter through `account/rateLimits/read`. Neither spends a model turn, and no token is
printed. The first act of a session is to read the percent; the last act is to read it again.

When no reader works, it asks once, in one line:

> I can't read the weekly window from here. What percent are we at, and back by what?
> One number is the reading and I'll set the mark from it; two numbers are the reading and the mark.

That is the Codex/ChatGPT wording. In Claude, the question uses **used**. The
agent follows your preference or actual display when it differs from these
defaults. It calculates and returns a boundary directly in the same terms:
**29% left, two points for the task → return with at least 27% left.**
Codex subtracts spending from left; Claude adds it to used. The meter adapter
translates a differently named transport field once at ingestion. Task reasoning
stays native; further conversion is needed only for a notation change or request.

A usable picture carries forward across tasks: the last real pulse plus
accounted work and an honest estimate. The agent asks for a refresh when it
matters, rather than making every task an intake form. The task allowance is
optional: give only used/left and the agent chooses and announces a bounded
allowance. As the lens learns your rhythm, that exchange becomes lighter.
The first real reading establishes the numerical boundary. While it is pending,
the agent keeps preparation small and complete.

The provider's meter or the owner's display supplies the real quota; the agent
accounts for the steps between pulses. A new reading replaces its extrapolation.
The owner continues to set task allowances and correct pace and priority. Both
the real reading and those corrections shape the next action and the lens.

## Reading the clock

| Harness | Limit that counts | How the agent reads it |
| --- | --- | --- |
| Claude Code | rolling 5-hour window, 7-day window behind it | `usage.py` reads the harness's own login; first and last act of a session |
| Codex CLI | weekly limit | `usage.py` asks `codex app-server` for `account/rateLimits/read` |
| Anything else | whatever the owner's display shows | asks once, in one line, together with the mark |

## The loop

| You supply | The agent does |
| --- | --- |
| `Back by 85` | Lands in a committed state and returns at or before 85% used, the return priced in. |
| Codex task with an available live meter | Reads the actual quota and reset itself, without asking you to copy the number. |
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
├── usage.py       Reads the clock: Claude Code's windows or Codex's live quota
└── LICENSE
```

The only runtime script is `usage.py`, standard library only. Human documentation,
evaluation cases, and release tooling stay in this repository.

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

Created by Daniil Demidko. Concept developed with Fable; two independent skill editions
prepared with Astra and with Fable, merged after a six-perspective Fable review and Astra's behavioral rehearsals. Released under the [MIT license](LICENSE).
