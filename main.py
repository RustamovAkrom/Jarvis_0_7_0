from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio
import webbrowser
from speech_recognition import Recognizer, Microphone

from fuzzywuzzy import fuzz
import yaml

from Asistent.recognition import (
    online_recognition_function,
    offline_recognition_function,
)
from Asistent.speach import speaker_audio, speaker_torch, speaker_windows
from Asistent.cmd import (
    control_volume,
    play_music,
    Search_On_Browser,
    Search_On_Wikipedia,
)

import settings
import time
import os

commands = dict(yaml.safe_load(open("commands.yaml", "rt", encoding="utf-8")))
search_commands = dict(
    yaml.safe_load(open("search_commands.yaml", "rt", encoding="utf-8"))
)


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


def filter_data(text: str, data: dict) -> dict:
    rc = {"commanda": "", "paracent": 0}
    for commanda, values in data.items():
        for x in values:
            vrt = fuzz.ratio(text, x)
            if vrt > rc["paracent"]:
                rc["commanda"] = commanda
                rc['ahk_path'] = values[0]
                rc["paracent"] = vrt
    return rc


def filter_search_activator(text: str):
    data = {}
    for command, value in search_commands.items():
        for v in value:
            if v in text:
                data["value"] = command
                data["search"] = text.strip(v)
    return data


def cmd(input_voices_cmd: str) -> None:

    searching = filter_search_activator(input_voices_cmd)

    # Searching system
    if searching:
        print(f"Search == <{searching}> completed...")

        if searching["value"] == "search_browser":
            try:
                Search_On_Browser(searching["search"], settings.DEFAULT_SEARCH_BROWSER)

            except Exception as ex:
                print(f"Error {ex}")
                speaker("not_found")

        elif searching["value"] == "search_wikipedia":
            try:
                # Speaker torch
                speaker_torch(Search_On_Wikipedia(searching["search"]))

            except Exception as ex:
                print(f"Connection error: {ex}")
                speaker("not_found")
        return

    # Commands system
    data_dict_in_filter = filter_data(input_voices_cmd, commands)

    if data_dict_in_filter["paracent"] >= 70:
        print(f"Commanda == <{input_voices_cmd}> completed...")

        commanda = data_dict_in_filter["commanda"]
        ahk_path = data_dict_in_filter["ahk_path"]
        
        if commanda == "music":
            speaker("ok")
            os.startfile(play_music(settings.MUSICS_DIR))

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

        elif commanda == "sound_min":
            speaker("ok")
            control_volume(25)

        elif commanda == "sound_max":
            speaker("ok")
            control_volume(100)

        elif commanda == "sound_50":
            speaker("ok")
            control_volume(50)

        elif commanda == "stupid":
            speaker("stupid")

        elif commanda == "thanks":
            speaker("thanks")

        elif commanda == "screenshot":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])
        
        elif commanda == "blocking":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])
        
        elif commanda == "sleep": 
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])
        
        elif commanda == "empty_path":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])
        
        elif commanda == "clipboard":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])

        elif commanda == "set_language":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])

        elif commanda == "rool_up_windows":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])
        
        elif commanda == "task_manager_open":
            speaker("ok")
            os.startfile(ahk_path['ahk_path'])

    else:
        speaker("not_found")


def recognitions_activator() -> None | str:

    if settings.ONLINE_RECOGNITION and settings.OFFLINE_RECOGNITION:

        voices_listen_input = None

        if online_recognition_function(recognizer, microphone)[1]:
            voices_listen_input = online_recognition_function()[0]

        elif offline_recognition_function(audio, res)[1]:
            voices_listen_input = offline_recognition_function(audio, res)[0]

        else:
            return voices_listen_input

        return voices_listen_input

    elif settings.OFFLINE_RECOGNITION:

        voices_listen_input_offline = offline_recognition_function(audio, res)

        if voices_listen_input_offline[1]:
            return voices_listen_input_offline[0]

        return None

    elif settings.ONLINE_RECOGNITION:

        voices_listen_input_online = online_recognition_function(audio, res)

        if voices_listen_input_online[1]:
            return voices_listen_input_online[0]

        return None
    print("Please activate on listening.")
    exit(1)


def main() -> None:
    speaker("run")

    ltime = time.time() - 1000

    while True:
        # try:
            voices_input = recognitions_activator()
            print(voices_input)

            for name in settings.ASISTENT_NAMES:
                if fuzz.ratio(voices_input, name) >= 70:
                    speaker("greet")

                    ltime = time.time()

                    while (
                        time.time() - ltime
                    ) <= settings.LISTEN_COMMANDS_SECCOUND_TIME:

                        voices = recognitions_activator()

                        if voices != "":
                            cmd(voices)

                        print("...")

        # except Exception as e:
        #     print("Error in main function.", e)
        #     exit(1)


if __name__ == "__main__":
    # offline recognition module
    model = Model(settings.OFFLINE_RECOGNITION_DIR)
    audio = PyAudio()
    res = KaldiRecognizer(model, 16000)

    # online recognition module
    recognizer = Recognizer()
    microphone = Microphone()

if __name__ == "__main__":
    main()

# offline_recognition_function(settings.OFFLINE_RECOGNITION_DIR)
