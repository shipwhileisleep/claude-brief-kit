# Planner brief: from a wish list to stages with done criteria

> Use this before a large build. A planning agent turns a short wish list into 5 to 8 stages.
> Each stage later becomes one subagent brief (brief.md), with its done_when as the Requirements.

## Read first
<files with the project context>

## Owner's request
<the wish list, quoted as the owner wrote it>

If the owner is away: "The owner cannot answer. Decide yourself and record every decision in <NOTES file>."

## Your task
Write a short design and split the work into 5 to 8 build stages, in build order.

Rules for the stages:
- Foundations before content: the structure that everything else depends on comes first.
- Each stage produces something that can be tried on its own.
- Risky or unknown parts get their own stage, early, so a failure shows up before the rest depends on it.
- The last stage is a full end-to-end test of the whole result.

Rules for `done_when`:
- Every condition can be checked by a script, a test or a measurement. No "looks good", no "feels right".
- Use numbers and ranges: counts, percentages, durations, sizes.
- Name the test or check that proves each condition.
- If something cannot be checked by a machine (taste, sound, look), say so and name who judges it.

Do not build anything. Read only.

## Time budget
<for example 45 minutes>. If time runs out, return the stages you have.

## Return format (JSON)
```json
{
  "design": "short summary of the design and the decisions you made",
  "stages": [
    { "name": "...", "goal": "what exists after this stage", "done_when": "measurable conditions" }
  ]
}
```

## Example of a good done_when (from the ASHEN HUNTER build, stage 4, boss Sevarog)
"All 14 move tests pass (7 attacks, passive takes damage, dodge takes none). sevarog_fight with the perfect bot
ends in victory, reaches phases 2 and 3, runs the Harvest once, uses at least 6 different attacks, keeps the hero
visible in at least 98 % of frames, reports no missing assets and no vanish anomalies, and lasts 120-300 s."
