import pyttsx3


def speaker_windows(what: str, gender: str = "male") -> None:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    if gender == "famale":
        try:
            engine.setProperty("voice", voices[2].id)

        except:
            engine.setProperty("voice", voices[1].id)

    elif gender == "male":
        engine.setProperty("voice", voices[0].id)

    else:
        print("Speaker gender error.")
        exit(1)

    engine.say(what)
    engine.runAndWait()


__all__ = ("speaker_windows",)
