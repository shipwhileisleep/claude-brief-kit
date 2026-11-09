# Claude Brief Kit

A free Claude Code skill that makes Claude write a clear one-page brief, with budgets and checkable goals, every time it hands work to a helper agent (a subagent).

It comes from the build of ASHEN HUNTER, a game made in Unreal Engine with Claude. The video: https://www.youtube.com/@shipwhileisleep

## Quick start

1. **Copy the folder.** Download this repository (on GitHub: green "Code" button, then "Download ZIP") and unzip it.
   Copy the folder `agent-briefs` into `~/.claude/skills/`. `~` means your home folder, and `.claude` is a hidden folder in it
   (on Windows: the `.claude\skills` folder inside your user folder).
   Create the `skills` folder if it does not exist. To use it in one project only, copy it to `.claude/skills/` inside that project.
2. **Start Claude Code** in a new session, so it picks up the skill.
3. **Ask for a big task**, for example: "Use subagents to build X in stages." Claude now writes a brief for each
   helper agent like the ones in `examples/`. You can also call the skill by name: `/agent-briefs`.

## What a brief looks like

```
Read first        files with the context, so the brief stays short
Goal              what exists when the agent is done
Owner's words     what you actually said, quoted
Reference         2 to 3 real examples to measure against
Requirements      each one with a done criterion a script can check
Machine rules     how to reach your tools, and what is known to break
Hard rules        what must never happen, and why
Budgets           time, tests, stop rule, checkpoint
Priorities        what comes first if time runs out
Deliverables      exact files, compatible with what they replace
Progress file     one line per finished piece
Return format     what the agent reports back
```

## Why these rules

All numbers are from the ASHEN HUNTER build.

- **Budgets.** One build stage ran 4 hours and was still not finished. Its brief said "keep earlier stages working
  (rerun their tests)" and had no time limit, so the agent replayed every old test after every change. A test with
  2 seconds of gameplay took almost 4 minutes.
- **Test budget and stop rule.** With a 90-minute time budget, a 25-minute test budget and the rule "test the new
  part where it is", the next stage was done in 74 of 90 minutes, with about 20 minutes of tests.
- **Critics without write access.** In the first review of the boss arena, two critics found 12 must-fix items.
  They were not allowed to change anything, so their only job was to find problems.
- **A reference to measure against.** The owner said the first game music sounded amateur and flat. The briefs for
  that music asked for loudness and loop measurements but named no real track to compare with. That is why the kit now
  has `reference.md`.
- **Prototype first, then the rest.** One boss theme was rebuilt as a test in 103 of 150 minutes. After the test piece and
  one revision, all music was rebuilt in 3 hours 29 minutes of a 6 hour 30 minute budget.
- **Measurable done criteria.** The sound effects brief asked for checks a script can run (for example "impacts must
  reach their onset within 5 ms"). 74 of 74 effect files passed.

Budgets are not a guarantee: the boss stage used 40 minutes of tests against its 25-minute test budget. It still
finished inside its 2-hour time budget, and the watchdog is there for the cases where it would not.

## What each file is for

| File | What it is for |
|---|---|
| `agent-briefs/SKILL.md` | Tells Claude when and how to write a brief. This is the skill. |
| `agent-briefs/templates/brief.md` | The one-page brief, with an example line under each heading |
| `agent-briefs/templates/planner.md` | Turns a short wish list into 5 to 8 stages, each with a checkable "done when" |
| `agent-briefs/templates/critic.md` | A reviewer with one role and one hard question, who may not edit anything |
| `agent-briefs/templates/test-policy.md` | Rules that keep testing short and targeted |
| `agent-briefs/templates/reference.md` | Collect and measure real examples before quality work |
| `examples/sound-effects.md` | Real brief: rebuild 74 sound effect files in Ableton |
| `examples/music-prototype.md` | Real brief: rebuild one music piece as a test, after "it sounds amateur" |
| `examples/test-policy.md` | Real brief text that fixed the 4-hour stage, with what went wrong before |
| `extras/CLAUDE-md-long-runs.md` | A short section for your CLAUDE.md with the rules for long runs |
| `extras/watchdog.md` | A timer that reports when an agent goes over its budget |
| `extras/ableton-osc/` | Optional: two extra commands for driving Ableton Live from Claude |

## Using it without the skill

You can use the templates by hand. Open `agent-briefs/templates/brief.md`, copy it into your message to Claude,
and fill in the headings, or ask Claude: "Write a brief for this task using this template: ..." The same works
for the planner, critic, test policy and reference templates.

## FAQ

**Does it work outside games?**
Yes. The skill is about handing work to helper agents. It works for any task you would split up: research,
writing, data work, code, music.

**Do I need Unreal or Ableton?**
No. Nothing in the kit needs them. The Ableton extra is optional and only useful if you want Claude to drive Ableton Live.

**Do I need to be a programmer?**
No. You copy one folder and talk to Claude as usual.

**What is a subagent?**
A second Claude that the first one starts for a part of the work. It starts with an empty memory and only knows
what the brief tells it.

**Will Claude always keep to the budget?**
Not always. That is what the watchdog in `extras/watchdog.md` is for: it reports when the time is up, so Claude
can stop the agent or ask it to finish.

## License

MIT, see `LICENSE`. The AbletonOSC handlers are an addition to [AbletonOSC](https://github.com/ideoforms/AbletonOSC), which is also MIT-licensed.
