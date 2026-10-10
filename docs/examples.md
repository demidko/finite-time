# Example conversations

Illustrative dialogue and arithmetic, not recorded measurements. Marks and prices
use percentage points of the full window. Conversation follows the owner's
interface: left for Codex/ChatGPT, used for Claude by default. An explicit owner
preference or displayed label takes priority. The agent calculates directly in
that system, subtracting spending from left or adding it to used.

## Codex: no numbers in the assignment

### With a live quota source

**Owner:** Refactor the parser and cover the new syntax.

The agent reads the authenticated Codex meter. In this example, the relevant
window reports 29% left. The owner's standing preference leaves the mark to the agent.

**Agent:** The live meter shows 29% left. The refactor prices at two points
with checks and saving; I'll land it with 27 left. Say another number if you
want it different.

### With no accessible quota source

**Owner:** Refactor the parser and cover the new syntax.

**Agent:** I can't read the weekly window from here. What percent are we at,
and back by what? One number is the reading and I'll set the mark from it; two
numbers are the reading and the mark.

**Owner:** 38% left. You decide.

**Agent:** No rate on this meter yet: I'll land the first parser piece with 37
left and price the rest from the reading there. Back with 37 left?

The first piece is priced alone because the meter has no rate yet; the reading
at its landing sets the rate, and the rest is priced then as a statement.

## Claude: current reading supplied; mark omitted

**Owner:** Update the migration guide. 62% used.

**Agent:** Priced at five points with link checks and saving. Back by 67?

**Owner:** ok.

The agent says the line once, as a question a single "ok" can answer, and
starts on the go. It does not ask how many points it may spend: the price is
its own count, and the mark follows from it.

## Claude: the next unit no longer fits as priced

**Owner:** 62% used. Consolidate the guide; return before 78%.

**Agent:** I'll work within those 16 points, with closure included. The first
unit is one complete section and its references.

**Owner, later:** 74% used.

The agent had priced the last section at three points and closure plus margin
at two; five points do not fit in four. The price is wrong, not the task: the
section's write and its link check fold into one call, the commit, the lens,
and the clock into another, and the section is two points with closure one.
It lands checked before 78. The agent does not close early with a required
section unwritten, and it does not call the guide complete before the section
is in.

## Claude: room before the mark

**Owner:** 10% used. Finish the cleanup; back by 15.

The agent lands the planned pieces at 12% used with two small items it had
priced at a point each still undone. Three points stand between it and the
mark. Returning now would be leaving early with the task undone, the plainest
planning failure: the window had the points. It finishes both items, checks,
commits, and returns at 14. Early is early only with done in front of it.

## Claude: the mark is short at the opening

**Owner:** 62% used. Rewrite all twelve sections of the guide in the house
style; return before 66%.

**Agent:** Twelve sections, a write apiece at half a point, and one for closure
is seven; the mark holds four, and a rewrite cannot be scripted below one call
a section. Six sections land by 66; the whole guide needs back by 69. Which?

This is the one moment the fit is discussed: before the first call, with the
arithmetic, and the scope is the owner's to cut by naming what to drop. A bare
"ok" takes 69, the one mark the agent proposed; "66" restated without a cut is
the whole guide by 66, the fit the agent's to make. Either way the question
does not come back.

## Codex: a fraction of the remainder

**Owner:** The weekly meter shows 40% left. Spend at most 20% of what remains.

**Agent:** Twenty percent of the remaining 40 points is eight points, so I'll
return with at least 32% left, with checks and saving included.

## The same mark in each interface

**Codex owner:** 29% left. Spend up to two points.

**Agent:** I'll return with at least 27% left, including checks and saving.

**Claude owner:** 62% used. Spend up to eight points.

**Agent:** I'll return before 70% used, including checks and saving.

The owner supplies the number as displayed; the agent keeps the response in
that same direction. If a Claude owner explicitly prefers left, the agent uses
left there too.

## A mark inside the reserve

**Owner:** 89% used. Return by 98%.

The reserve is the owner's to give, and the number wins: the mark is 98. The agent prices the
return itself as the last step, keeps that many calls short of 98, and where the script runs it
re-reads the clock before every atom instead of trusting its count. It does not spend the last
points merely to reach 98 if the task finishes earlier.

## A lesson that changes the installed skill

After comparable sessions show the same problem, a lens entry might become:

> In long-context documentation passes, integration and link checks exceeded
> the first closure estimate twice. Keep one directory per unit and price
> integration before admitting the next directory. Confidence: provisional.

This is an example of compact decision learning. The installed lens records
only observations that actually occurred for its owner.
