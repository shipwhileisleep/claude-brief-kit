# Long agent runs (paste this section into your CLAUDE.md)

> CLAUDE.md is the file Claude Code reads at the start of every session.
> Your personal one is ~/.claude/CLAUDE.md; a project one sits in the project folder.
> Copy everything below the line into it.

---

## Long agent runs

- Every subagent, workflow or long task gets a time budget and a test budget in its prompt.
  Over budget means: stop, write down what is left, return.
- Tests run at the place of the new feature. No full regression run after every step.
  Rerun an old test only if the change touches what it covers. Do not rerun a passing test unchanged.
- Slow steps (builds, restarts, exports, renders) are batched so they happen as rarely as possible.
- Reviews are done by separate critics without write access, in parallel, on one shared recording or result.
  The critics judge that result; they do not each replay or rebuild the work.
- Start a watchdog next to every run that is longer than about 15 minutes, for example a background
  `sleep <budget in seconds>; echo "BUDGET exceeded: <task>"`. When it fires, check the progress file and intervene.
- Every long task writes a progress file with one timestamped line per finished piece.
- Give honest time estimates. Say how sure you are, and update the estimate when it changes.
- When time is short, leave out deliverables that were not asked for, and say so.
