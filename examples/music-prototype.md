# Example: one music piece as a budgeted prototype (real brief, lightly edited)

> Written by the orchestrating Claude Code session during the ASHEN HUNTER build (brief B16 in the video),
> right after the owner said the game music sounds amateur and flat.
> Edits: private paths, the host name and the owner's name were replaced; one line about another program was shortened.
> Result: done in 103 of 150 minutes. Later follow-up messages to the same agent rebuilt all music in 3 h 29 min
> of a 6 h 30 min budget.
> What is missing: a reference. The brief says "think dark orchestral hybrid" but names no real track to
> measure against, so every check compared the music with its own old version. templates/reference.md adds that step.

First read PROJECT_NOTES.md (project context, the ASHEN HUNTER campaign paragraph), then game/AUDIO.md (the whole audio pipeline: decisions, recording run, faults and fixes).

GOAL: one prototype music piece for the game ASHEN HUNTER that sounds professionally produced. Rebuild only the Sevarog boss theme, state phase2 (F sharp minor, 128 BPM, 32 bars, current stems sv_drums, sv_timp, sv_lowstr, sv_soul, sv_brass, sv_choir; composition in scripts/audio/comp_aj.py, the laptop copy is in Pipeline\musik). The owner listened to the current loops and said: it sounds amateur, the instruments sound very flat, hardly any effects are used, everything sounds flat. He wants his installed Ableton instruments and effects used. The current version is game/music_preview/MU2_sevarog_phase2.mp3; listen-analysis is up to you (spectrum, dynamics, stereo width), but nobody can listen for you, so judge by production technique and measurements.

What I diagnosed as the causes (verify and extend):
- Notes have near-constant velocities (vel() with +-4 spread), no crescendos, no phrase dynamics, no volume or filter movement.
- One shared dark hall (Hybrid Reverb) and a Glue Compressor; no saturation, no early-reflection room vs. long tail depth staging, no stereo widening, no bus processing, no sub or impact layers.
- Instruments are basic Core Library racks (Cello Strings, Ensemble Strings, Choir Pad Avalon, Voicelike Pad) plus Orchestral Brass, Orchestral Mallets and Drum Booth packs.

What to do (your judgment on details; aim for modern epic game-boss music, think dark orchestral hybrid):
- Arrangement: sections with real build-up and release across the 32 bars (it must still loop seamlessly, see the two-pass loop method in AUDIO.md), ostinato strings, counter line, brass stabs/braams, choir swells, percussion with fills and accents, impacts and risers at section changes, a sub layer.
- Expression: velocity arcs and phrase dynamics; per-stem volume or filter movement (clip envelopes or device parameter automation through AbletonOSC if possible, otherwise gain curves in post_aj and say so).
- Sound: layer sources (e.g. strings with a synth pad or Wavetable/Operator layer, brass with a low synth braam, timpani with Drum Booth toms and a synthesized boom), use Live 12 Suite devices: EQ Eight, Saturator, Roar, Drum Buss, Glue Compressor, Compressor with sidechain ducking where it helps, Echo, Hybrid Reverb with separate short room and long hall, Chorus-Ensemble or Utility width, Spectral/Granulator textures if useful. Installed extras: Spitfire LABS (Amplified Cello Quartet, Pedal Pads, Synth Pads, Ondes Musicales, Monochord, Guitar Harmonics, Glass Piano, Soft Piano, Dulcimer, Mandolin), Decent Sampler, KV_Element, GOLDEN Piano. Do NOT use ValhallaVintageVerb (demo build). AUDIO.md section 11 says plug-in probes failed earlier; LABS through OSC may or may not load; spend at most 15 minutes on it and fall back to Live devices.
- A mix bus: route or resample the summed stems through a final chain (EQ, glue compression, gentle saturation, limiter) in Live, or record the stems and apply bus processing in Live afterwards. Target -17 LUFS integrated for the game state, true peak at or below -1.5 dBFS, punchy rather than squashed.
- The game imports a premixed stereo loop per state (see AUDIO.md and game/scripts/s6). Keep stems too so base (subset) and phase2 can still be built, but only phase2 must be done in this prototype.

Constraints:
- Ableton Live 12.2 Suite is already open on the laptop (ssh user@laptop), AbletonOSC on 127.0.0.1:11000. Use the existing pipeline (live_aj.py, render_aj.py, post_aj.py with the fixes from section 11). Long jobs run as scheduled tasks with -LogonType Interactive (see AJ_Rec2 / aj_rec2.cmd and the notes in AUDIO.md); the end of an ssh session kills child processes. Only delete Live tracks with your own prefixes. Do not close Live. Do not touch Unreal, the game project or other running programs. C: has only 13 GB free: keep temporary WAVs small and clean them up.
- Do not overwrite the current game files or out\ premixes. Write new files to a new folder, e.g. Pipeline\musik\out_v3\ on the laptop.
- TIME BUDGET: 150 minutes total. TEST BUDGET: at most 20 minutes of checks (loudness, peak, seam, clipping, dropout check on the new takes only). Recording is in real time; plan for at most 2 full recording passes. If you exceed the budget, stop, write down what remains, and return.
- Write in plain ASCII, no dashes as sentence punctuation.

Deliverables:
1. On this server: game/music_v3/ with sevarog_phase2_v3.mp3 (192 kbps, the loop played twice so the seam is audible), the old version as sevarog_phase2_v2.mp3 for A/B, the new stems as mp3 if under 30 MB total, and a short CHANGES.md listing every concrete production change (instruments, layers, devices with key settings, automation, bus chain) and the measurements (LUFS, true peak, crest factor, stereo correlation, spectrum balance compared with the old version).
2. A new section 12 in game/AUDIO.md and the changed scripts copied to game/scripts/audio/ (keep the old versions working for the other pieces).
3. Return value: what changed, the measurements old vs new, what you could not do and why, how long it took, and how long you estimate rebuilding the other 5 pieces and 7 stingers the same way would take.
