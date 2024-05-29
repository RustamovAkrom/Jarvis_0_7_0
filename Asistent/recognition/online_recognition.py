from speech_recognition import (
    Recognizer,
    Microphone,
    WaitTimeoutError,
    UnknownValueError,
    RequestError,
)


recognizer = Recognizer()
micraphone = Microphone()


def online_recognition_function() -> str:
    """Online recognition on module speach_recognition russian"""

    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 1000
    recognizer.pause_threshold = 0.5
    answer = None
    active = True

    try:
        with micraphone as source:

            recognizer.adjust_for_ambient_noise(micraphone, duration=0.5)

            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            except WaitTimeoutError:
                print("Can you chek if yor micraphone is on, please")
                answer = None
                active = False

            try:
                answer = recognizer.recognize_google(audio, language="ru-RU").lower()

            except UnknownValueError:
                print("Unknown value error")
                answer = None
                active = False

            except RequestError:
                print("Connection error")
                answer = None
                active = False

            return (answer, active)

    except:
        return (answer, active)


__all__ = ("online_recognition_function",)
