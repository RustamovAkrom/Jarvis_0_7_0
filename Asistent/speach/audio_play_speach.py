import pygame
import random


def speaker_audio(name: str, audio_files_dir: str, audio_files: dict) -> None:
    for wav_file in audio_files.keys():
        if name == wav_file:

            pygame.init()
            try:
                pygame.mixer.music.load(audio_files_dir + audio_files[name])
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

            except pygame.error as e:
                print("error playing audo", e)

            finally:
                pygame.mixer.quit()
                pygame.quit()
