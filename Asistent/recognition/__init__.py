from .offline_recognition import *
from .online_recognition import *


def recognitions_activator(
    offline_recognition_model_path: str,
    offline_recognition: bool,
    online_recognition: bool,
) -> None | str:

    if online_recognition and offline_recognition:

        voices_listen_input = None

        if online_recognition_function()[1]:
            voices_listen_input = online_recognition_function()[0]

        elif offline_recognition_function(offline_recognition_model_path)[1]:
            voices_listen_input = offline_recognition_function(
                offline_recognition_model_path
            )[0]

        else:
            return voices_listen_input

        return voices_listen_input

    elif offline_recognition:

        voices_listen_input_offline = offline_recognition_function(
            offline_recognition_model_path
        )
        if voices_listen_input_offline[1]:
            return voices_listen_input_offline[0]

        return

    elif online_recognition:

        voices_listen_input_online = online_recognition_function()
        if voices_listen_input_online[1]:
            return voices_listen_input_online[0]

        return
