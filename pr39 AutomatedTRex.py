import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(280, 430):
        for j in range(220, 380):
            if data[i, j] < 100:
                hit("down")
                return

    # Draw the rectangle for cactus
    for i in range(280, 430):
        for j in range(420, 470):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 5 seconds")
    time.sleep(5)

    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))

        # # Draw the rectangle for cactus
        # for i in range(300, 420):
        #     for j in range(420, 470):
        #         data[i, j] = 0
        #
        # # Draw the rectangle for birds
        # for i in range(300, 420):
        #     for j in range(220, 380):
        #         data[i, j] = 171
        #
        # image.show()
        # break