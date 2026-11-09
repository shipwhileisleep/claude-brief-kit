# Two extra AbletonOSC handlers (optional)

You only need this if you want Claude to drive Ableton Live over OSC. Nothing else in this kit depends on it.

[AbletonOSC](https://github.com/ideoforms/AbletonOSC) is an MIT-licensed control surface script
that lets programs control Ableton Live with OSC messages. These two handlers are an addition to it, written during
the ASHEN HUNTER build when stock AbletonOSC could not do two things the music needed:

| Message | What it does |
|---|---|
| `/live/aj/envelope` | Writes a whole automation curve for one device parameter into a clip, in one message |
| `/live/aj/audio_clip` | Puts an audio file from disk into a clip slot |

They were tested with Ableton Live 12.2 Suite. The names start with `aj` because of the game's working title;
you can rename them.

## Install

1. Install AbletonOSC as its README describes (it lives in your Live "Remote Scripts" folder, for example
   `Documents\Ableton\User Library\Remote Scripts\AbletonOSC` on Windows).
2. Open `AbletonOSC/abletonosc/view.py` in a text editor. Keep a backup copy of the file.
3. Open `handlers.py` from this folder. Copy the lines between `BEGIN extra handlers` and `END extra handlers`.
4. Paste them at the very end of the `init_api` function in `view.py`, after the last `add_handler` line.
   Keep the indentation exactly as it is (8 spaces), the same as the lines above it.
5. Reload: send the OSC message `/live/api/reload` to Live (port 11000), or restart Live.

## `/live/aj/envelope`

Arguments, in this order:

1. track index (0 is the first track)
2. clip slot index (0 is the first slot)
3. device index on that track (0 is the first device)
4. parameter index on that device (on most devices 0 is "Device On")
5. step length in beats (0.25 is one sixteenth note at 4/4)
6. and following: the values, one per step, starting at beat 0 of the clip, in the parameter's own range

The clip must already exist. Any old envelope for that parameter is cleared first.
Live answers with track, slot, device, parameter and the number of steps written.
In the build, 2048 steps of 1/16 beat per loop were accepted in one UDP message.

## `/live/aj/audio_clip`

Arguments: track index, clip slot index, full path to an audio file (WAV or AIFF) on the computer that runs Live.
The track must be an audio track and the slot must be empty. Warping is switched off, so the file plays at its
original speed. Live answers with track, slot and the clip length in beats.

## Example (Python, with the python-osc package)

```python
from pythonosc.udp_client import SimpleUDPClient

live = SimpleUDPClient("127.0.0.1", 11000)

# filter cutoff on track 2, clip slot 0, device 1, parameter 3: a rise over 4 beats in 16 steps
values = [0.2 + 0.05 * i for i in range(16)]
live.send_message("/live/aj/envelope", [2, 0, 1, 3, 0.25] + values)

# load a rendered file into track 5, clip slot 0
live.send_message("/live/aj/audio_clip", [5, 0, "C:/music/riser.wav"])
```

AbletonOSC sends its answers back to port 11001 on the sending computer.

## Notes from the build

- Live does not answer OSC while it loads a preset; in the build this took 30 seconds and more (37 s for Timpani).
  Use long timeouts for messages that follow a preset load.
- Plug-in instruments that choose their sound in their own window cannot be set up over OSC. Live's own devices
  and presets work.

## License

AbletonOSC is MIT-licensed (copyright its authors). The handlers in this folder are released under the MIT license
of this repository.
