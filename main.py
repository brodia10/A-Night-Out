import os
import sys
from time import sleep

from playsound import playsound

import menu
from console_writer import ConsoleWriter
from scene_controller import SceneController
from scenes import one_a, three_a, three_b, two_a, two_b

# Instantiate Class Objects
console = ConsoleWriter()
scene = SceneController()

if __name__ == "__main__":

    # Print credits and game menu
    print(menu.title_banner)
    playsound("audio/theme.wav", False)
    sleep(0.5)
    print(menu.credits_1)
    sleep(0.5)
    print(menu.credits_2)
    print("")
    print("")
    sleep(0.5)
    print("")
    print("")

    # console.write(f"{menu.instructions} \n", effect=False)
    scene.start(one_a, two_a, two_b)
    scene.start(two_a, three_a, three_b)

