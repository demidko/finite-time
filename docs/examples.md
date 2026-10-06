# Example conversations

Illustrative dialogue and arithmetic, not recorded measurements. Task allowances
use percentage points of the full window. Conversation follows the owner's
interface: left for Codex/ChatGPT, used for Claude by default. An explicit owner
preference or displayed label takes priority. The agent calculates directly in
that system, subtracting spending from left or adding it to used.

## Codex: no numbers in the assignment

**Owner:** Refactor the parser and cover the new syntax.

**Agent:** How much of your nearest quota window is left, and how many
percentage points may this task spend? You can give just left; I'll plan
the allowance.

**Owner:** 38% left. You decide.

**Agent:** I'll provisionally allocate eight points and return with at least
30% left, including checks and saving. I'll first price the smallest parser
change against the current window.

The eight-point choice needs to follow the actual task and available evidence;
it is not the skill's universal default.

## Claude: current reading supplied; allowance omitted

**Owner:** Update the migration guide. 62% used.

**Agent:** How many percentage points should this task use? I can choose the
allowance from the work if you prefer.

**Owner:** Choose it.

**Agent:** I'll use up to five points and return by 67% used, including link
checks and saving.

The agent asks once. It does not keep requesting an allocation after the owner
leaves that decision to it.

## Claude: the next unit no longer fits

**Owner:** 62% used. Consolidate the guide; return before 78%.

**Agent:** I'll work within those 16 points, with closure included. The first
unit is one complete section and its references.

**Owner, later:** 74% used.

If the agent estimates that another complete section costs three points and
closure plus uncertainty costs two, five points will not fit in the remaining
four. It closes the reached state, reports which required sections remain,
and returns. It does not call the whole guide complete.

## Codex: a fraction of the remainder

**Owner:** The weekly meter shows 40% left. Spend at most 20% of what remains.

**Agent:** Twenty percent of the remaining 40 points is eight points, so I'll
return with at least 32% left, with checks and saving included.

## The same allowance in each interface

**Codex owner:** 29% left. Spend up to two points.

**Agent:** I'll return with at least 27% left, including checks and saving.

**Claude owner:** 62% used. Spend up to eight points.

**Agent:** I'll return before 70% used, including checks and saving.

The owner supplies the number as displayed; the agent keeps the response in
that same direction. If a Claude owner explicitly prefers left, the agent uses
left there too.

## Reserve released explicitly

**Owner:** 89% used. Return by 98%.

With the default ten-point reserve still in force, the effective boundary is
90%. The agent starts closure and explains that only one gross point is
available before the protected reserve.

**Owner:** You may use my reserve for this task. Return by 98%.

The boundary is now 98%. The agent recalculates from the current reading and
closes within that boundary. It does not spend the last points merely to reach
98% if the task finishes earlier.

## A lesson that changes the installed skill

After comparable sessions show the same problem, a lens entry might become:

> In long-context documentation passes, integration and link checks exceeded
> the first closure estimate twice. Keep one directory per unit and price
> integration before admitting the next directory. Confidence: provisional.

This is an example of compact decision learning. The installed lens records
only observations that actually occurred for its owner.
