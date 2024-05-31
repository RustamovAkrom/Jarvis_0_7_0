import webbrowser
import wikipedia

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import datetime
import random
import os


def control_volume(volume_: int) -> None:
    """Controler volume windows system 'volume_': int = 1 equil windows volume 1%"""

    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_ / 100, None)


def play_music(
    path: str, random_start: bool = True, path_number: int = 0
) -> None | str:
    """Play music on dir musics fayles if random_start: bool = False to play music on path_number: int = 0, (index, 0) music play"""

    if not os.path.exists(path):
        return f"({ path }) does not exist. !"

    music_list = os.listdir(path)
    music_count = int(len(music_list))

    if random_start:
        play_random_musik = random.randint(0, music_count)
        path = f"{ path }/{ music_list[play_random_musik] }"

    else:
        path = f" { path }/{ music_list[path_number] }"

    return path


def Search_On_Browser(search: str, search_browser: str) -> None:
    f"""Searching and open browser in url ({search_browser})"""

    webbrowser.get().open(search_browser + search)


def Search_On_Wikipedia(search: str) -> str:
    """return text searching on wikipedia summary"""

    wikipedia.set_lang("ru")
    page = wikipedia.page((search))
    page.html
    return page.summary
