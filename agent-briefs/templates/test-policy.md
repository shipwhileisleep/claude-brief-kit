# Test policy (paste into every build brief)

> Without this block, agents tend to retest everything after every change.
> In the ASHEN HUNTER build that made one stage run 4 hours. Adjust the numbers to your task.

TEST POLICY:
- Test budget: about <25> minutes of test wall time for this task. Keep to the time budget in the task.
  When the time budget is used up, stop, write down what is unfinished in <NOTES file> and return.
  Note what you skipped.
- Test new features at their location. Jump straight to the new part (a shortcut, a debug start option,
  a small test input) and run short checks. Do not start from the beginning for every test.
- Do not rerun earlier stages' full test suites. Rerun an earlier test only if you changed code it covers.
- Do not rerun a passing test unchanged.
- Run logic tests at minimum cost: small inputs, low quality settings, no graphics if the test does not
  need pixels. Use full quality only for the few outputs that judge the look or sound.
- Batch slow steps (builds, restarts, exports) so they happen as rarely as possible.
- At the end: one short smoke test of the whole thing, then the newest part once.
- When you wait for something, check every 30 to 60 seconds, and put a timeout on every wait.
- An earlier attempt of this task may have left processes running and partial work on disk:
  check first, close stray processes you or that attempt started, and reuse finished work.
- Report test time separately in your return: "tests took about N of M minutes".
