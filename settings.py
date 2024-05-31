################################################################################################################
#############################################Jarvis 0.7.0#######################################################
################################################################################################################
from pathlib import Path
import random

from dotenv import load_dotenv
import os

load_dotenv(".env")

# Build paths inside the project like this: BASE_DIR / "sundir".
BASE_DIR = Path(__file__).resolve().parent

# Offline recognition model dir
OFFLINE_RECOGNITION_DIR = "modules/vosk-model-small-ru-0.22"  # russian small model.

# Asistent config
ASISTENT_NAMES = ("джарвис", "чарльз")
MULTIPART_SPEACH_ASISTENT_NAME = "aidar"
ONLINE_RECOGNITION = False  # is online recognition listen.
OFFLINE_RECOGNITION = True  # is offline recognition listen.
LISTEN_COMMANDS_SECCOUND_TIME = 20  # listen command sec.

# proposals dirs settings.
TELEGRAM_DIR = os.getenv("TELEGRAM_DIR")
YOUTUBE_DIR = os.getenv("YOUTUBE_DIR")
GOOGLE_DIR = os.getenv("GOOGLE_DIR")
BROWSER_DIR = os.getenv("BROWSER_DIR")
MUSICS_DIR = os.getenv("MUSICS_DIR")

# Searching default browser.
DEFAULT_SEARCH_BROWSER = "https://www.google.com/search?q="


# Default asistent speaker config.
SPEAKER_1 = {
    "ACTIVE": True,  # speaker activator
    "AUDIO_FILES_DIR": "Asistent/media/",  # speaker audio files dir.
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

# Windows operation system speaker config.
SPEAKER_2 = {
    "ACTIVE": False,  # speaker activator.
    "GENDER": "famale",  # speaker gender (male or famale).
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
