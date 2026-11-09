---
name: agent-briefs
description: Write a one-page brief before delegating work. Use whenever you start a subagent (Agent tool), a workflow, a background job or any long multi-step task for another Claude, and when you plan a large build in stages. The brief gives the agent files to read first, a goal, the owner's own words, measurable done criteria, machine and hard rules, a time budget, a test budget, a stop rule, priorities, swap-compatible deliverables, a progress file and a fixed return format. Also covers stage planning, critics without write access, a targeted test policy and measuring against a reference before quality work.
---

# Agent briefs

A subagent starts with an empty memory. It knows only what you write. Before you start any subagent,
workflow or long task, write a brief with `templates/brief.md` (in this skill's folder).

## Steps

1. Big task with several parts: first run a planning agent with `templates/planner.md`. It returns 5 to 8
   stages, each with a measurable `done_when`. Each stage then gets its own brief.
2. Quality work (music, sound, visuals, writing style): first follow `templates/reference.md`. Collect 2 to 3
   references, measure them, write the gap, prototype one piece, and let the owner judge it before the rest.
3. Write the brief with every heading of `templates/brief.md`. Write "none" under a heading that does not
   apply. Paste `templates/test-policy.md` into every brief that builds or changes something.
4. After a build step, review with 2 or 3 critics from `templates/critic.md`, in parallel, on the same recorded
   material. Give the merged must_fix list to one fix agent.
5. Start a watchdog next to every agent that runs longer than about 15 minutes (see below).
6. Tell the user what you started, the budget, and an honest estimate. Say what is uncertain.

## Rules for every brief

- Read first: point to files and sections instead of pasting long context.
- Quote the owner's words (translated if needed), so the agent sees what was really asked.
- If the owner is away, say so: "The owner cannot answer. Decide yourself and record every decision."
- Done criteria must be checkable by a script, a test or a measurement. Use numbers and ranges.
- An agent cannot see or hear like a person. Make it measure (screenshots, frame counts, loudness, peaks),
  say in the report what nobody has looked at or listened to, and leave taste to the owner.
- Every brief has a time budget, a test budget and a stop rule: "When the time is used up, stop, write down
  what is left, and return." Long tasks also get a checkpoint ("At 2 h, if X has not started, fall back to Y").
- Never write "rerun all earlier tests" or "keep everything working" without limits. Test the new part at its
  location; rerun an old test only if you changed what it covers.
- List priorities for the case that time runs out, most important first, and say what happens to the rest.
- Deliverables keep the names, formats and lengths of what they replace, so the next step can swap them in.
- A progress file gets one timestamped line per finished piece, so the work survives an interruption.
- Hard rules state the reason ("Never save X: saving would erase its references").
- Carry earlier failures forward as rules ("an earlier clip played black: use Main profile and yuv420p").
- Time-box risky side quests: "Spend at most 15 minutes on it, then fall back to Y."
- Parallel agents get scope fences: "Step 3 is NOT your job: do not touch A or B."
- Ask for a fixed return format: what was done, what was skipped and why, measurements, test time,
  time used, an estimate for the rest, file locations.

## Watchdog

Next to each long agent, start a background command that waits for the time budget and then prints a line:

```bash
sleep 5400; echo "BUDGET exceeded: stage 3 (90 min)"
```

Run it in the background (Claude Code notifies you when it finishes). When it fires: read the agent's progress
file, then either tell the agent to wrap up and return, or stop it, or extend the budget once and tell the user.
If the agent returns early, stop the watchdog.
