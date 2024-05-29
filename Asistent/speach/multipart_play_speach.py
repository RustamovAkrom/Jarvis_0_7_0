import sounddevice
import torch
import time

# torch settings
language = "ru"
modle_id = "v3_1_ru"
sample_rate = 48000
speaker = "aidar"
put_accent = True
put_yo = True

device = torch.device("cpu")  # cpu or gpu

model, text = torch.hub.load(
    repo_or_dir="snakers4/silero-models",
    model="silero_tts",
    language=language,
    speaker=modle_id,
    trust_repo=True,
)

model.to(device)


def speaker_torch(what: str) -> None:
    audio = model.apply_tts(
        text=what + "..", speaker=speaker, put_accent=put_accent, put_yo=put_yo
    )

    sounddevice.play(audio, samplerate=sample_rate + 1.05)
    time.sleep((len(audio) / sample_rate) * 0.5)
    sounddevice.stop()


__all__ = ("speaker_torch",)
