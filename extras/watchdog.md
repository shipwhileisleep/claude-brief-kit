# The simplest watchdog

An agent that runs over its budget does not notice it by itself. In the ASHEN HUNTER build, one stage ran
4 hours, and the orchestrating session noticed it too late. A watchdog is a timer that runs next to the agent and reports when the budget
is used up.

## Start it

When Claude starts a long agent, it also starts this command in the background (Claude Code's Bash tool has a
"run in background" option and tells Claude when the command finishes):

```bash
sleep 5400; echo "BUDGET exceeded: stage 3 (90 min)"
```

5400 is the budget in seconds (90 minutes x 60). If you want some slack, use the budget plus 30 %.

You do not have to type this yourself. The `agent-briefs` skill and the CLAUDE.md section in this folder tell
Claude to do it. You can also ask: "Start a watchdog for this agent with a 90-minute budget."

## When it fires

1. Read the agent's progress file. How far is it, and is it still making progress?
2. Then choose one:
   - Nearly done: tell the agent to finish the current piece, write down the rest and return.
   - Stuck or going in circles: stop the agent and keep what it finished.
   - Good progress and the rest is important: extend the budget once, start a new watchdog, and tell the user.
3. Write the overrun into the notes, so the next brief has a more realistic budget.

## When the agent returns early

Stop the watchdog, so it does not fire for a task that is already finished.
