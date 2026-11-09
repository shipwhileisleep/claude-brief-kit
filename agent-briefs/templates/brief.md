# Subagent brief: <short task name>

> One page. The subagent starts with an empty memory and knows only what is written here.
> Fill every heading. If a heading does not apply, write "none" so the agent knows it was considered.
> Lines in italics are examples, most of them from a real build; replace them.

## Read first
Files that hold the context, so this brief can stay short. Point to sections, do not paste them.
*Read PROJECT_NOTES.md (the audio section), then AUDIO.md sections 4 and 12.*

## Goal
One or two sentences: what exists when the agent is done, and where this task sits in the larger plan.
*Rebuild the game's 28 sound effects in Ableton Live. This is step 2 of 3; step 3 (import into the game) is not your job.*

## Owner's words
The owner's actual feedback or request, quoted (translated if needed). The agent sees what was really asked.
*"It sounds amateur, the instruments sound very flat, hardly any effects are used."*

## Reference
What to measure the result against: 2 to 3 real examples and the measured gap. See reference.md.
*Two released boss themes in the same genre. Measure their loudness range and energy above 4 kHz the same way as ours, and close the gap.*

## Requirements
What the result must do, each with a done criterion that a script or a measurement can check.
*Impacts reach their onset within 5 ms. Loops keep their exact sample length and loop without a click.*

## Machine and tool rules
How to reach the machines and tools, and what is known to break.
*Long or GUI jobs run as scheduled tasks; the end of an ssh session kills child processes. Wrap every ssh call in `timeout`.*

## Hard rules (never do)
Things that must not happen, with the reason, so the agent does not reason around them.
*Never save Lvl_Moor: saving would erase its references. Do not close programs you did not start.*

## Budgets
- Time: total wall time from the agent's start.
- Tests: how much of that time may go to checks, and which checks (see test-policy.md).
- Stop rule: what to do when the time is used up.
- Checkpoint: a point in the middle where the agent must decide to continue or fall back.
*Time 2 h 15 min. Tests: one measurement pass per group. At 2 h stop starting new work, fill the rest with the old files, write the report and return.*

## Priorities if time runs out
The order in which to do the work, most important first, and what to do with the rest.
*Boss effects first, then the sword, then enemies, then ambience. Anything not redone keeps its old file.*

## Deliverables
Exact files and folders. Keep names, formats and lengths compatible with what they replace, so the next step can swap them in.
*Output to out_v5_sfx/ with the same file names, channel counts and sample rate as the old files, plus manifest.json.*

## Progress file
One timestamped line after each finished piece, so the work survives an interruption.
*Write the start time and one line per effect group to sfx_v5/PROGRESS.md as you go.*

## Return format
What the agent hands back, in a fixed order, short.
*What was done, what was skipped and why, measurements old vs new, how long it took, an estimate for the rest, file locations.*
