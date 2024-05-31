from vosk import KaldiRecognizer
from pyaudio import PyAudio, paInt16
import json


def offline_recognition_function(audio: PyAudio, res: KaldiRecognizer) -> None | str:
    """Offline recognition on module vosk russian"""
    stream = audio.open(
        format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000
    )

    stream.start_stream()

    answer = None
    active = True

    while True:
        try:
            data = stream.read(4000)

        except:
            active = False

        if len(data) == 0:
            break

        if res.AcceptWaveform(data):
            answer = json.loads(res.Result())

            return (answer["text"], active)


__all__ = ("offline_recognition_function",)
