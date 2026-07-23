import os
import random
import pygame
from pygame import mixer

from Features.clap_d import *


# ============================================================
# PILOT AI - CLAP MUSIC CONTROL
# ============================================================

# Automatically detect project root
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Music folder inside project
MUSIC_FOLDER = os.path.join(BASE_DIR, "DATA", "MUSIC")


def play_random_music(folder_path=MUSIC_FOLDER):

    # Check whether music folder exists
    if not os.path.exists(folder_path):
        print(f"Music folder not found: {folder_path}")
        return

    music_files = [
        file
        for file in os.listdir(folder_path)
        if file.lower().endswith(
            (".mp3", ".wav", ".ogg", ".flac")
        )
    ]

    if not music_files:
        print("No music files found.")
        return

    selected_music = random.choice(music_files)

    music_path = os.path.join(
        folder_path,
        selected_music
    )

    try:
        pygame.init()
        mixer.init()

        print(f"Pilot AI playing: {selected_music}")

        mixer.music.load(music_path)
        mixer.music.play()

        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        mixer.music.stop()
        mixer.quit()

    except Exception as error:
        print(f"Error playing music: {error}")


def clap_to_music():

    print("Pilot AI clap detection started.")

    while True:

        tt = TapTester()
        clap_count = 0

        while True:

            if tt.listen():

                clap_count += 2

                if clap_count >= REQUIRED_CLAPS:

                    print("Clap detected. Starting music...")

                    play_random_music()

                    break


if __name__ == "__main__":
    clap_to_music()