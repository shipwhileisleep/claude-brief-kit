# Example: the test policy that fixed a 4-hour stage (real brief text, lightly edited)

> Written by the orchestrating Claude Code session during the ASHEN HUNTER build (brief B9 in the video).
> Edits: private paths and the details of the interrupted run were removed.

## What went wrong before
The earlier stage brief (B6) said: "Build it, test it on the running game, keep earlier stages working (rerun their tests), ..."
It had no time budget. So after every change the agent replayed every earlier test, from the start of the game, inside
the editor, at about a tenth of real time. A test with 2 seconds of game time took almost 4 minutes, a fight test with
112 seconds of game time took 20 minutes, and stage 2 ran for 4 hours without finishing. The owner: "this takes far too long."

## The block that went into every build brief afterwards

TEST POLICY (the owner said the run takes far too long; testing ate most of stage 2: a full rerun of all earlier test batches, editor restarts, and runs at roughly 10 times slower than real time):
- Budget about 25 minutes of test wall time for this task, and keep to the time budget in YOUR TASK. When the time budget is used up, stop, record what is unfinished in NOTES.md and return. Note in NOTES.md what you skipped.
- Batch C++ edits into as few builds as possible; restart the editor only after a C++ build. Iterate on Python, data and assets with the editor running.
- Test new features at their location: put the hero directly at the encounter or boss (teleport, set checkpoint, debug start option) and run short sims. Do not walk from the game start for every test.
- Do not rerun earlier stages' full test batches. Rerun an earlier test only if you changed code it covers. At the end, one smoke run: start the game, check the log for errors and missing assets, jump to the newest content and play it once with the bot.
- Logic tests at minimum cost: small window, lowest scalability (sg.*Quality 0, r.ScreenPercentage 50), or -nullrhi if the test does not need pixels. Use full quality only for the few screenshots and clips that judge the picture.
- Do not rerun a passing test unchanged. Poll at 30 to 60 s intervals.
- An aborted attempt of this same task may have left an editor, game or build process running and partial work on disk: check first, close stray processes, and reuse finished work.

## The task lines that came with it (each stage got its own time budget)

- "YOUR TASK (time budget 90 minutes): finish stage 2 by fixing lockon_multi, respawn and game_morrvak only, then build stage 3."
- "YOUR TASK (time budget 2 hours): build stage 4."
- "YOUR TASK (time budget 60 minutes): a reduced stage 5. Light and dress zones A, C and D so that nothing looks like grey blockout in the camera view ... Skip anything else from the full stage."

## Result
- Stage 2 finish plus stage 3: 74 of 90 minutes, tests about 20 minutes, one C++ build. The agent: "I stayed in the 90-minute budget, and tests took about 20 minutes. I made one C++ build and reran no earlier test batch."
- Stage 4 (boss Sevarog): 105 of 120 minutes. Not perfect: "testing took about 40 minutes against the 25-minute budget, and I needed three builds instead of one".
- Stage 5: 63 of 60 minutes.
