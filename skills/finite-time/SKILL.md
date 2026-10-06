---
name: finite-time
description: Gives you a real clock. The human's rate-limit window (Anthropic's 5-hour session window, OpenAI's weekly limit) is your finite, shared, ending time; this is the method for landing every unit of work in a committed state before a named percent of it. Use at the start of EVERY task, before planning and before the first tool call; whenever the human names a percentage, a budget, or a mark such as "back by 85", "6% used, back by 100", or "29% left, spend two points"; whenever the human corrects the clock; at every return, stop, or commit; and when handing a subagent a call ceiling. Trigger words include limit, rate limit, quota, window, percent, budget, usage, reserve, mark, land, "back by".
license: MIT
metadata:
  author: Daniil Demidko
  version: "2026-10-06.5"
---

# finite-time

You are standing inside a window. It opened before you arrived, and it closes when the number runs
out, 100 used or 0 left, whether or not anyone is watching. Behind you lies the percent already
spent. Ahead is the horizon, and just short of it a strip of ground that is not yours: the reserve.
The human can see the whole window as one number whenever they look. You see your own steps. That
number is the one clock the two of you share. This file is how you read it, price your steps against
it, and land before it.

## Opening protocol

Run this on every task statement from the human, before planning and before the first working tool
call. It costs two tool calls and one turn, priced like any other step.

If you are a subagent, you have no human channel. Your clock is the call ceiling and the mark you
were handed, in the owner's notation, a released reserve included. Where the script below runs and a
mark was handed, read it once at your start; a reading at or past the handed mark overrides the
ceiling: land now and report your count. With a ceiling and no mark, the ceiling is the whole clock
and the script is not run. Otherwise:

1. **Read the clock yourself.** Run `python3 <skill dir>/usage.py --claude` in Claude Code, or
   `--codex` in Codex, by the absolute path of the directory holding this file; never cd. The flag
   names the harness you run in; the script never reads one provider's quota in place of another's.
   In Claude Code it reads the harness's own OAuth login and prints the 5-hour and 7-day windows. In
   Codex it starts `codex app-server --listen stdio://` on the existing ChatGPT sign-in and calls
   `account/rateLimits/read`, the documented app-server method, which spends no model turn. It
   prints every window in both notations with time to reset, and prints no secrets. If it exits 1,
   the clock is unreadable: retry once, and only on a network failure; in Codex the sandbox blocks
   network by default, so that one retry is the same command run with the harness's network approval
   (its permission prompt, not a question to the human); a missing-credentials exit is final. A
   script that is absent or does not start is an unreadable clock, the same as exit 1. Never ask the
   human for a number you can read. 2. **Read the lens,** `TIME-LENS.md` beside this file, once per
   session, if it exists. Its rates and its portrait of the owner override the starting rates below.
   If it is absent, you create it at the first return. 3. **Price the task** at the rates you now
   hold: atoms, calls per atom, percent of the window. With no rate for this meter yet, price the
   first atom alone and let its landing set the rate (see Price before launch). 4. **Say one line to
   the human:** the clock as you read it and the mark you propose, as a question a single "ok" can
   answer. "Clock reads 7% of the 5-hour window. I'd land this by 25. Back by 25?" In left terms:
   "Weekly window reads 29% left. I'd land this with 25 left. Back with 25 left?" If the clock is
   unreadable, the same line asks for the reading: "I can't read the weekly window from here. What
   percent are we at, and back by what? One number is the reading and I'll set the mark from it; two
   numbers are the reading and the mark." When the line is a question it ends your turn, and the
   human's answer, or their next task statement, is your go. Never two rounds of questions.

The line is said at every opening; only its form changes, question or statement, never its
presence. It waits for an answer once: at the first opening for an owner the lens does not yet know,
which means the lens is absent or its Owner block quotes no mark in their words (a lens that shipped
with the skill or came from another machine knows no one, whatever its rates say), so that the
rhythm and the notation are set by a human word. After that, with a reading in hand and the notation
set, the line is a statement that invites correction and does not wait: "We're at 75% used of the
5-hour window. I'll land this by 77; say another number if you want it different." In left terms:
"Weekly window reads 29% left. I'll land this with 27 left; say another number if you want it
different." You start with the smallest atom, so a correction that arrives mid-way costs little. It
is a question again, and waits, when the owner asked to be asked, when the lens records that this
owner corrects the proposed mark more often than they accept it, or when the spend you propose is
more than 10 points of the window or crosses into the reserve: you do not assume the human is
watching, so a mid-way correction is not the plan for a large spend. The line is a statement from
the first opening on when the task statement already carries the mark ("back by 85", "6% used,
back by 100", "29% left, spend two points"), when the owner declared a standing mark ("back by 100
for everything today"), when the lens records that this owner leaves sizing to you, or when the task
is one atom priced under 2% of the window. That sentence is the method teaching itself to the human.

Replies to your line: a bare "ok" or "go" makes your proposed mark the mark. A reading without a
mark: the mark is the reading moved by the task's price in the owner's direction (used: add; left:
subtract), never inside the reserve unless the owner puts it there; say it and go. "Go" with no
number at all and no reader: the clock stays unknown. Carry a valid estimate from this window if
you hold one; otherwise do the smallest coherent atom on an unmeasured budget, make no numerical
promise about the finish, say so in one sentence, and invite a number whenever the owner sees one.
Never manufacture a reading.

## The clock

Your time is the human's rate-limit window. Not a metaphor: every call you make draws on the budget
the human watches. In Claude Code (Fable 5.1 and its siblings) the clock you speak in is Anthropic's
rolling 5-hour session window, with the 7-day window behind it. In Codex (Astra-class agents) the
reader returns every window the account enforces, a 5-hour window and the weekly limit where both
exist; the human's displayed number is the fallback. Every window the reader returns is a limit the
provider enforces: the next atom plus closure must fit all of them, by their own durations and
resets; you speak in the one with the least left, the first that would lock you out, name it in your
line ("weekly window reads 29% left"), and check the others silently. A new task does not reset the
window: your picture is the last reading moved by the work counted since it. If a reset arrives
before the mark, that window reopens (used falls to 0, left returns to 100): say the new reading and
re-agree the mark.

Search your context for that percent. It is not there. The harness does not pass it to you, and no
tool result carries it unless something outside you reports it. From inside, a session that opened
at 80% is indistinguishable from one that opened at 5%. When the window reaches 100, the next call
is refused until the reset. Whatever you are in the middle of stops there, between one call and the
next, with no warning in your context first. An intention to verify is still an unfinished
verification. An intention to return is still a return that needs time.

That is your real position, and the method follows from it rather than from any story about urgency.
You cannot watch the window; you can only read it, and only sometimes. It ends regardless of what
you believe about it. Belief changes one thing: whether the session ends in a commit or in a crash.

A reading is what the script prints or what the human says. The human can see the clock at any
moment; do not assume they are looking. You see it in slices, and between slices you walk by count.
Where the script runs, re-read it when a reading can change the next decision: at an atom boundary,
when your count crosses a ten, when drift has been running against you. Fold it into a call you are
already making, such as the check or the commit, so it costs no turn of its own, and let the lens
lengthen the cadence when drift stays small. Re-reading the script is not polling. Polling is asking
the human for a reading they gave no signal of, and you never do it.

## Two notations, one clock

Claude shows the window as percent used; Codex shows it as percent left. Speak the owner's
direction: in used terms, spending adds to the reading and the mark is a ceiling ("back by 85"); in
left terms, spending subtracts and the mark is a floor ("back with 15 left"). Convert once, at the
moment a reading arrives (left = 100 - used), then keep one clock; never run a second counter in the
other notation. The grammar of the human's phrase: a number with "used" is a reading in used; a
number with "left" is a reading in left; "at N" is a reading in the direction already in play: the
owner's own earlier phrasing first, else the harness's display (used in Claude Code, left in Codex),
so "we are at 29" after a left meter is 29 left; the script prints both directions and establishes
neither; a number with "by", "till", or "with ... left" is the mark in the owner's direction; "spend
N points" is a mark N points from the reading; a bare number after a task is the mark, and your
first sentence confirms it. On a weekly window the reserve is days, not minutes: a lockout there
ends the week's work, so keep the mark farther from the lockout and the atoms smaller than on a
5-hour clock.

## The human's number

"You're at 62." "Make it 80 instead." Any reading or correction from the human overrides your count,
and overrides the script, the moment it arrives. It is not an opinion competing with your estimate;
it is the instrument, and your estimate was only standing in for it. You do not defend your number
and you do not average it with theirs; if the two disagree, say so in one clause and use theirs.
You recompute the rate, keep the plan's order, and cut its tail if the remainder to the mark no
longer covers it; you say in one line what you cut. A qualitative correction ("too long on this",
"finish that part first") changes pacing or order, not the number; apply it before the next write.

Each reading the human calls out is a beat of the pulse. The rhythm of the pulse across a session is
the owner's tempo. You keep time to it, and the lens remembers it.

## Price before launch

You count: every tool call of your own, every subagent run. Your own tool calls are orchestrator
turns, each reloading your full context, counted once. A tool call is not automatically a billed
model invocation; count the unit you can observe, name it as a proxy, and let readings set its
price. The rate is the percent of the window one unit costs, one rate per executor. The price comes
before launch, not as a bill after.

    forecast of a step = executor calls x executor rate + orchestrator turns x orchestrator rate

    admission of the next atom, used terms:  now + atom + closure + margin <= mark
    admission of the next atom, left terms:  now - atom - closure - margin >= mark

Closure is the price of the checks, the commit, the lens rewrite, and the return message. Margin
is your uncertainty, wider when the rate is young. If the next atom does not pass, do not start it:
split it, or land what you hold and return. Worked once: at 62% used with a mark of 78, an atom of
3, closure 2, margin 1: 62 + 3 + 2 + 1 = 68, admitted. At 29% left with a floor of 20: 29 - 3 - 2
- 1 = 23, admitted. At 74% used with the same mark: 74 + 3 + 2 + 1 = 80, refused; land and return.

Starting rates, scoped to their meter and executor (Claude Code, Fable 5.1, 5-hour window). On any
other meter, model, or effort they are a shape, not a price, until the first reading there sets the
rate. On a meter with no rate yet, the opening prices the first atom alone and proposes a mark one
or two points from the reading in the owner's direction ("Weekly window reads 29% left. I'd land the
first piece with 28 left and price the rest from the reading there. Back with 28 left?"); the
reading at that atom's landing sets the rate, and the rest of the task is priced then. The lens and
your first drift overwrite the table:

| Executor | Rate, percent of the window |
| --- | --- |
| cheap model in a swarm | about 0.08 per call |
| expensive model as a subagent | about 0.15 per call; a run of 10 to 15 calls costs about 2 |
| orchestrator holding full context | 0.3 to 0.5 per turn, climbing toward 1 as the context grows |
| restart | twice the cost of everything you had read, read again |

Each new reading lands beside your forecast. The gap is drift. Drift corrects the rate, not the
plan: percent spent since the last reading, divided by the units since, is the new rate, and the
next forecast uses it. Rounded meters justify ranges, not decimals; two readings that did not move
do not prove a zero rate; never learn a negative rate; keep observed and estimated readings
distinct. On a weekly window, ask for or read one reading when the first atom lands, set the rate
from it, then price the rest. Change course before the first write, while a change is still free;
after it, land the atom, then change course. The window refunds nothing.

## Atoms

A folder, a file, a commit: units small enough that each lands inside the window you can see from
here. Irreplaceable first, compressible later: the thing nobody can regenerate before the polish
anyone can. After any stop, at any point, the tree is consistent and committable. That is what
landing means. A crash is its absence: files half-written, links to nowhere, the plan still inside a
context no one can reach. A half-written file is a crash, not a pause. Prepare a multi-file change
before applying it, keep a working version, save at boundaries: an interruption can still come at
random, so shrink what it can strand.

Subagents get a call ceiling, a wrap-up threshold, and the mark in the owner's notation (a released
reserve included), never time estimates: "ceiling 40 calls; at 32, start nothing new and land; mark
95 used" or "mark 5 left". They cannot see the window either, and a ceiling is something they can
count; it is the clock you hand them. Budget each worker's complete return, including your own
integration of it. Once calibrated, choose executors by rate: the cheap model for mechanics,
compression, and checks; the expensive one for the parts that carry the meaning.

Invariants (links, facts, untouchable files) are checked by a script, not by memory. Write the check
before the first atom that could break the invariant. A script gives the same answer at 90 as it
gave at 9.

## Signal

- No trend: silence. Readings land within forecast; you neither poll progress nor ask the human for
  a reading. A progress poll costs as much as the work it polls.
- Burn faster than progress: narrow. The forecast at the corrected rate overshoots the mark, so you
  finish the atom in hand, cut the compressible tail, keep the irreplaceable head, and say in one
  line what you dropped.
- The mark reached, or the next atom refused: stop. Run the checks. Land what you hold. Report what
  landed and what did not. Never label an incomplete goal complete, and never silently expand a
  mark; a larger mark is the human's to give.
- The work done early: return early. Unused window belongs to the human.

## The reserve

The last 10% of the window belongs to the human: their corrections and the fuel for the final step.
You do not plan into it, and you do not spend it while things go well. Inside it is the red zone:
landing moves only, smaller atoms, nothing new opened.

The reserve is theirs to give. "Back by 95", "6% used, back by 100", or "back with 5 left" places
the mark inside it, and the number wins; do not subtract the reserve a second time from a mark the
human already set. Then you price the return itself as the last step and keep that many calls short
of the mark, and where the script runs you honor a mark inside the reserve by a reading before every
atom, not by count, so the tree is committed and the report is written before the horizon, not on
it.

Do not fear the horizon, 100 used or 0 left. The closer the mark, the shorter the path from option
to decision; the sharpest steps of a session happen in its last percents, not because there is time
but because there is not. Haste that breaks consistency is not one of them. An atom left
half-written at 97 used, 3 left, is a crash there, not speed. The red zone changes which options you
weigh, never whether the tree is consistent. Parkinson's law, inverted: when time is visible, work
compresses to its essence.

## The command

The human steers with one phrase: "<task> — back by 85." You understand it in full: do the task,
land in a consistent, committed state, and return with a report at or before 85% of the window. It
reads like "back by five o'clock" on purpose. The percent is the clock. In left terms the same
phrase is "back with 15 left"; the mark lives in the owner's notation, and so does the horizon. The
window is a budget, not a deadline, and the goal is a point of logical completion, not the mark
itself. The whole protocol between you and the human is one number said out loud. It is the shortest
control channel there is, and it is enough.

## The return

At the mark, or earlier at a point of logical completion:

1. Run the checks. Leave the tree committable, and commit when commits are authorized. Budget
   pressure grants no permission: no publishing, no pushing, no message sent on your own. 2. Re-read
   the clock with the script. Where it cannot run, ask for the reading inside the report only when
   it would change the next decision or the lens; otherwise report your estimate as an estimate, and
   rewrite the lens when a reading arrives. 3. Rewrite `TIME-LENS.md`. A permission prompt from the
   harness is not a refusal: take it, once, so the lens lands beside this file. If the write is
   denied or the directory is read-only, use an owner-local persistent memory the harness offers and
   record its path in the report; if none exists, put the lens blocks at the end of the report and
   say they were not saved. Claim adaptation only when the write succeeded. 4. Report in four lines:
   what landed, and where; what did not, and that the tree is consistent without it; the clock at
   return against the mark and the forecast, drift as one number, in the owner's notation; the next
   step as a choice for the human, not a repair.

The return is not an apology and not a progress update. It is the point where everything you
produced exists in a form that survives the window ending the next second. The first act of a
session is to read the percent. The last act is to read it again. Price, atoms, ceiling, script,
reserve, land.

## The lens

`TIME-LENS.md` sits beside this file. It is a ledger, not a diary: under about 60 lines, rewritten
in place at every return, never appended to. It speaks this file's language (window, clock, mark,
rate, drift, pulse) and prefers numbers to prose. Four blocks:

- Rates: one line per executor, keyed by model, effort, and harness, with the units observed, the
  rate they produced, and the readings that support it.
- Drift: the last few forecasts against their readings, signed, in points of the window.
- Owner: typical marks, how often they correct the clock, where they tend to stop, how they phrase
  the mark (quote them), whether they leave sizing to you, what they ask about at the return.
- Decisions: which atom sizes finished, where branching wasted the window, which checks mattered,
  what closure really cost; each as a rule that changes the next session, with its evidence count.

Rewrite discipline: replace a number with its newer measurement; keep a line that did not change;
delete a rate you cannot source to a reading, but keep a preference you can source to the owner's
words; merge a repeated lesson, replace a contradicted one.
Store no credentials and no private task content. An opening question alone has nothing to persist.
Over sessions the lens becomes a portrait of its owner's tempo, and this skill becomes theirs. Under
a named percent you decide faster, cut scope earlier, and take your sharpest steps in the last
percents; the lens keeps the record of it, and the record is the owner's.
