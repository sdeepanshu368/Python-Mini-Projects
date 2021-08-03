from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("files/reminderlog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("files/reminder.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 15*60
    eyessecs = 30*60
    exsecs = 60*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'done' to stop the alarm.")
            musiconloop('files/reminder.mp3', 'done')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'done' to stop the alarm.")
            musiconloop('files/reminder.mp3', 'done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'done' to stop the alarm.")
            musiconloop('files/reminder.mp3', 'done')
            init_exercise = time()
            log_now("Physical Activity done at")
