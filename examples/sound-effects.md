# Example: rebuild the sound effects in Ableton (real brief, lightly edited)

> Written by the orchestrating Claude Code session during the ASHEN HUNTER build (brief B22 in the video).
> Edits: private paths, host names and the owner's name were replaced; one line about another tool was removed
> and one line about another program was shortened.
> Result: about 1 hour of the 2 h 15 min budget; 74 of 74 files passed the final check.

Read PROJECT_NOTES.md first (the ASHEN HUNTER paragraph), then game/AUDIO.md sections 4, 5.2, 12 and 13. They describe the project, the laptop, Ableton Live and the recording pipeline you will reuse.

## Task
Redo the game's sound effects in Ableton Live 12 Suite on the owner's laptop, replacing the current Python-synthesised effects. The owner's feedback on the old audio was that it sounds flat, amateur, with hardly any effects processing. The music has just been rebuilt in Live (AUDIO.md section 13); the effects are step 2 of 3. Step 3 (import into Unreal and video recording) is NOT your job: do not touch Unreal, the game project or the audio event table.

Scope: all effects in AUDIO.md 5.2 (28 effect names, 71 variant files incl. loops and the three ambience beds). The authoritative list with file names, kind, channels, lengths and loop flags is the laptop file `Pipeline\musik\out\manifest.json`; the current files are `out\sfx\*_NN.wav`.

## Requirements
- Output to `Pipeline\musik\out_v5_sfx\` with exactly the same file names, channel counts, sample rate and kind as the old files, so the integrator can swap the folder. Lengths: one-shots may differ by at most +-20 %, but `sev_comet_fall` must still end at its impact, loops must keep their exact sample length and loop seamlessly (check the seam step like check_aj.py does), impacts must reach their onset within 5 ms. Also write `out_v5_sfx\manifest.json` (copy of the old one with any changed lengths updated) and a check report.
- Sound: sources and processing from Live: Drum Booth, Orchestral Mallets, Voice Box (whispers, breaths, grunts can come from vocal chops processed hard), Suite synths (Operator, Wavetable, Drift, Meld, Sampler with Core Library sounds), Core Library one-shots and textures, Granulator II. Processing: Roar, Saturator, Drum Buss, Hybrid Reverb, Echo, Spectral Resonator/Time, Corpus, EQ Eight, pitch and transient shaping. Layer each impact (transient + body + tail), give the fire sounds crackle and air, give Sevarog's attacks weight (sub, distorted low layer, long dark tail). You may also run the old Python files through Live chains as one layer, but every effect must get real Live sources and processing, not only a re-render of the old file.
- Do not use the ValhallaVintageVerb demo plugin. Normalise one-shots to -1.2 dBTP as before; keep the loop and bed loudness close to the old values in 5.2 (within 2 LU).
- Priorities, in this order, in case time runs out: Sevarog effects (sev_*), Cinderbrand (cb_*), Husk and Caster and Brute, shrine/wall/brazier/UI, ambience beds. Any effect not redone keeps its old file copied into out_v5_sfx so the folder is always complete; list those clearly.

## Laptop and tools (details in AUDIO.md and PROJECT_NOTES.md)
- `ssh user@laptop` (Windows). PowerShell: write .ps1 files, scp to the helper folder on the laptop, run with `powershell -NoProfile -ExecutionPolicy Bypass -File`. Long or GUI jobs as scheduled tasks with -LogonType Interactive (the end of an ssh session kills child processes). Wrap every ssh/scp in `timeout`.
- Live 12.2 Suite is open with AbletonOSC on 127.0.0.1:11000 (custom handlers /live/aj/envelope and /live/aj/audio_clip). Pipeline scripts in `Pipeline\musik` (live_v3.py, render_v3.py, post_v3.py, measure_v3.py, run_queue_v4.py), Python C:\Python311\python.exe. Copies on the server in game/scripts/audio/. Known pitfalls from section 13.4: copy takes only after the size is stable, delete stale .asd files before loading a clip, check take lengths, record piano/choir-heavy material in small batches.
- Mute the Windows master output while recording (the helper script aj_mute.ps1; restore afterwards to its previous state; Live's internal recording does not depend on it).
- Another program uses about 8 GB RAM: leave it alone. Do not close or kill processes you did not start. C: has about 6 GB free: delete your raw takes when done. The server disk has 4 GB free: keep server-side copies small.
- Do not save Lvl_Moor, do not use the old self-made assets folder (irrelevant here, you do not open Unreal).

## Deliverables on the server
- `game/sfx_v5/`: a montage mp3 of all new effects (each new variant 1 after the old variant 1, with a short gap; old file stays unchanged on the laptop) plus PROGRESS.md (one timestamped line per effect group, update as you go) and the check report. Keep it under 30 MB.
- AUDIO.md: add section 14 (what was built per effect, chains, measurements, faults, what is not done). Copy new scripts to game/scripts/audio/.
- Write in plain ASCII, no dashes as sentence punctuation.

## Budgets
- Time budget: 2 h 15 min from your start. At 2 h stop starting new effects, fill out_v5_sfx with old files for the rest, write the report and return. Note the start time in PROGRESS.md.
- Test budget: per effect group one measurement pass (loudness, peak, onset, seam for loops, length) with a focused script; one re-record per failed take at most, then use the old file and note it. No repeated full check runs beyond one final pass over the whole folder.

## Return
A short report: what was redone, what kept the old file and why, measurements summary, faults, laptop state (mute restored, Live state, disk free), file locations.
