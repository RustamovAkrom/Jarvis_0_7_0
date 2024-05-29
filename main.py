from fuzzywuzzy import fuzz
import yaml

from Asistent.recognition import recognitions_activator, offline_recognition_function
from Asistent.speach import speaker_audio, speaker_torch, speaker_windows
from Asistent.cmd import control_volume

import settings
import time
import os

commands = dict(yaml.safe_load(open("commands.yaml", "rt", encoding="utf-8")))


def speaker(what: str) -> None:

    if settings.SPEAKER_1["ACTIVE"]:
        speaker_audio(
            what,
            settings.SPEAKER_1["AUDIO_FILES_DIR"],
            settings.SPEAKER_1["AUDIO_FILES"],
        )

    elif settings.SPEAKER_2["ACTIVE"]:
        speaker_windows(settings.SPEAKER_2["SPEAK"][what], settings.SPEAKER_2["GENDER"])

    else:
        print(what)


def filter_commands(text: str) -> dict:
    rc = {"commanda": "", "paracent": 0}
    for commanda, values in commands.items():
        for x in values:
            vrt = fuzz.ratio(text, x)
            if vrt > rc['paracent']:
                rc['commanda'] = commanda
                rc['paracent'] = vrt
    return rc


def cmd(input_voices_cmd: str) -> None:
    print(f"Commanda == {input_voices_cmd}")    

    data_dict_in_filter = filter_commands(input_voices_cmd)
    if data_dict_in_filter['paracent'] >= 70:

        commanda = data_dict_in_filter['commanda']
        print(commanda)
        if commanda == "music":
            return
            
        elif commanda == "music_next":
            return

        elif commanda == "music_off":
            return

        elif commanda == "music_prev":
            return

        elif commanda == "off":
            speaker("off")
            exit(1)

        elif commanda == "open_browser":
            speaker("ok")
            os.startfile(settings.BROWSER_DIR)

        elif commanda == "open_google":
            speaker("ok")
            os.startfile(settings.GOOGLE_DIR)

        elif commanda == "open_youtube":
            speaker("ok")
            os.startfile(settings.YOUTUBE_DIR)

        elif commanda == "open_telegram":
            speaker("ok")
            os.startfile(settings.TELEGRAM_DIR)

        elif commanda == "sound_off":
            speaker("ok")
            control_volume(0)

        elif commanda == "sound_on":
            speaker("ok")
            control_volume(60)

        elif commanda == "stupid":
            speaker("stupid")

        elif commanda == "thanks":
            speaker("thanks")

        else:
            speaker("not_found")
    else:
        speaker("not_found")


def main() -> None:
    speaker("run")

    ltime = time.time() - 1000

    while True:
        try:
            voices_input = recognitions_activator(
                settings.OFFLINE_RECOGNITION_DIR,
                settings.OFFLINE_RECOGNITION,
                settings.ONLINE_RECOGNITION,
            )
            print(voices_input)
            for name in settings.ASISTENT_NAMES:
                if fuzz.ratio(voices_input, name) >= 70:
                    speaker("greet")

                    ltime = time.time()

                    while (time.time() - ltime) <= settings.LISTEN_COMMANDS_SECCOUND_TIME:
                        voices = recognitions_activator(
                            settings.OFFLINE_RECOGNITION_DIR,
                            settings.OFFLINE_RECOGNITION,
                            settings.ONLINE_RECOGNITION,
                        )
                        cmd(voices)

        except Exception as e:
            print("Error in main function.", e)
            exit(1)

if __name__ == "__main__":
    main()

# offline_recognition_function(settings.OFFLINE_RECOGNITION_DIR)
