import os
import sys
from time import sleep

from playsound import playsound

import menu
from console_writer import ConsoleWriter
from scene_controller import SceneController
from scenes import one_a, three_a, three_b, two_a, two_b


if __name__ == "__main__":
    # Instantiate Class Objects
    console = ConsoleWriter()
    scene = SceneController()

    # Print credits and game menu
    print(menu.title_banner)
    playsound("audio/theme.wav", False)
    sleep(.5)
    print(menu.credits_1)
    sleep(.5)
    print(menu.credits_2)
    print("")
    print("")
    sleep(0.5)
    print("")
    print("")

    # When user enters 's' start the game
    if scene.validate_user_input("s", menu.instructions):
        # console.write(one_a.msg)
        console.write(one_a.img, effect=False)
        scene.que_next_scene(one_a, two_a, two_b)
