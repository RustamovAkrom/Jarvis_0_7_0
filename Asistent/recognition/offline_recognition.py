from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
import json
import os


def offline_recognition_function(model_path) -> None | str:
    """Offline recognition on module vosk russian"""

    if not os.path.exists(model_path):
        print(
            "Please download the model from:\n"
            "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder."
        )
        exit(1)

    model = Model(model_path)
    audio = PyAudio()
    res = KaldiRecognizer(model, 16000)

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
