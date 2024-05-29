################################################################################################################
#############################################Jarvis 0.7.0#######################################################
################################################################################################################
from pathlib import Path
import random

# Build paths inside the project like this: BASE_DIR / "sundir"
BASE_DIR = Path(__file__).resolve().parent

# Offline recognition model dir
OFFLINE_RECOGNITION_DIR = "modules/vosk-model-small-ru-0.22" # russian small model

# proposals dir settings
TELEGRAM_DIR = "C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Telegram Desktop/Telegram.lnk"
YOUTUBE_DIR = "C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Приложения Chrome/YouTube.lnk"
GOOGLE_DIR = "C:/Program Files (x86)/Google/Chrome/Application/chrome"
BROWSER_DIR = "C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Yandex.lnk"
MUSICS_DIR = "D:/videos"

# Searching default browser
DEFAULT_SEARCH_BROWSER = "https://www.google.com/search?q="

# Asistent settings
ASISTENT_NAMES = ("джарвис", "чарльз")
MULTIPART_SPEACH_ASISTENT_NAME = "aidar"
ONLINE_RECOGNITION = False  # Online recognition listen
OFFLINE_RECOGNITION = True  # Offline recognition listen
LISTEN_COMMANDS_SECCOUND_TIME = 15  # seccund

# Default asistent speaker
SPEAKER_1 = {
    "ACTIVE": True,  # speaker activator
    "AUDIO_FILES_DIR": "Asistent/media/",  # speaker audio files dir
    # audio files control settings
    "AUDIO_FILES": {
        "thanks": "thanks.wav",
        "stupid": "stupid.wav",
        "run": "run.wav",
        "off": "off.wav",
        "not_found": "not_found.wav",
        "ok": f"ok{ random.choice([1, 2, 3, 4]) }.wav",
        "greet": f"greet{ random.choice([1, 2, 3]) }.wav",
    },
}

# Windows operation system speaker
SPEAKER_2 = {
    "ACTIVE": False,  # speaker activator
    "GENDER": "famale",  # speaker gender (male or famale)
    # speak (russian text == famale), (english text == male) values "SPEAK".
    "SPEAK": {
        "thanks": "всегда к вашим услугам сэр",
        "stupid": "очень тонкое замечание сэр",
        "run": "доброе утро",
        "off": "отключаю питания",
        "not_found": "чего пытаетесь добиться сэр",
        "ok": random.choice(
            ["есть", "загружаю сэр", "запрос выполнен сэр", "загружаю сэр"]
        ),
        "greet": random.choice(
            ["всегда к вашим услугам сэр", "да сэр", "к вашим услугам сэр"]
        ),
    },
}
