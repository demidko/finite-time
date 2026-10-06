# Example conversations

Illustrative dialogue and arithmetic, not recorded measurements. All percentage
points refer to consumption of the full displayed quota window unless stated
otherwise.

## No numbers in the assignment

**Owner:** Refactor the parser and cover the new syntax.

**Agent:** How much of your nearest quota window is used or left, and how many
percentage points may this task spend? You can give just used/left; I'll plan
the allowance.

**Owner:** 38% left. You decide.

**Agent:** That is 62% used. I'll provisionally allocate eight points and return
by 70% used, including checks and saving. I'll first price the smallest parser
change against the current window.

The eight-point choice needs to follow the actual task and available evidence;
it is not the skill's universal default.

## Current reading supplied; allowance omitted

**Owner:** Update the migration guide. 62% used.

**Agent:** How many percentage points should this task use? I can choose the
allowance from the work if you prefer.

**Owner:** Choose it.

**Agent:** I'll use up to five points and return by 67% used, including link
checks and saving.

The agent asks once. It does not keep requesting an allocation after the owner
leaves that decision to it.

## The next unit no longer fits

**Owner:** 62% used. Consolidate the guide; return before 78%.

**Agent:** I'll work within those 16 points, with closure included. The first
unit is one complete section and its references.

**Owner, later:** 74% used.

If the agent estimates that another complete section costs three points and
closure plus uncertainty costs two, five points will not fit in the remaining
four. It closes the reached state, reports which required sections remain,
and returns. It does not call the whole guide complete.

## Used and left; total and remainder

**Owner:** The weekly meter shows 40% left. Spend at most 20% of what remains.

**Agent:** That is 60% used. Twenty percent of the remaining 40 points is eight
points, so I'll return by 68% used with checks and saving included.

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
