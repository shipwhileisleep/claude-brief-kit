# Two extra handlers for AbletonOSC (https://github.com/ideoforms/AbletonOSC).
# Paste the block between BEGIN and END at the end of ViewHandler.init_api() in abletonosc/view.py.
# The surrounding lines only show where it goes; they are already in view.py.
# Tested with Ableton Live 12.2 Suite. See README.md in this folder.

from typing import Optional, Tuple
from .handler import AbletonOSCHandler


class ViewHandler(AbletonOSCHandler):
    def init_api(self):
        # ... the existing handlers of view.py stay here ...

        # ---- BEGIN extra handlers ----
        def aj_envelope(params: Optional[Tuple] = ()):
            """track, slot, device, parameter index, step length in beats, values... -> one step per value, from beat 0"""
            t, s, d, j = (int(x) for x in params[:4])
            step = float(params[4]); vals = params[5:]
            track = self.song.tracks[t]
            clip = track.clip_slots[s].clip
            p = track.devices[d].parameters[j]
            clip.clear_envelope(p)
            env = clip.automation_envelope(p)
            if env is None: env = clip.create_automation_envelope(p)
            for i, v in enumerate(vals): env.insert_step(i * step, step, float(v))
            return (t, s, d, j, len(vals))

        def aj_audio_clip(params: Optional[Tuple] = ()):
            t, s, path = int(params[0]), int(params[1]), str(params[2])
            slot = self.song.tracks[t].clip_slots[s]
            slot.create_audio_clip(path)
            c = slot.clip
            c.warping = False
            return (t, s, float(c.length))

        self.osc_server.add_handler("/live/aj/envelope", aj_envelope)
        self.osc_server.add_handler("/live/aj/audio_clip", aj_audio_clip)
        # ---- END extra handlers ----
