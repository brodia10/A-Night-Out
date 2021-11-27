import os
import sys
from time import sleep

from playsound import playsound

import menu
from console_writer import ConsoleWriter
from scenes import one_a, three_a, three_b, two_a, two_b



def get_user_input(msg):
    user_input = input(msg)
    return user_input


# def choose_scene(current_scene, next_scene_a, next_scene_b):
#     selected_choice = ""
#     choices = {
#         "a": {
#             "choice" : current_scene.choices["a"]["choice"],
#             "img" : current_scene.choices["a"]["image"],
#         },

#         "b": {
#             "choice" : current_scene.choices["b"]["choice"],
#             "img" : current_scene.choices["b"]["image"],
#         },
#     }


#     prompt = get_user_input()

#     if get_user_input(f"1: {choice_a}") == "1":
#         selected_choice = choice_a
#         display_message(next_scene_a.msg)
#     elif get_user_input(f"2: {choice_b}") == "2":
#         selected_choice = choice_b
#         display_message(next_scene_b.msg)
#     else:
#         "Please enter a valid choice, 1 or 2"
#         choose_scene(current_scene, next_scene_a, next_scene_b)


if __name__ == "__main__":
    print(menu.title_banner)
    playsound("audio/theme.wav", False)
    sleep(0.5)
    print(menu.credits_1)
    sleep(0.5)
    print(menu.credits_2)
    print("")
    print("")
    sleep(0.5)
    if get_user_input(menu.instructions) == "s":
        # playsound("audio/theme.wav", False)
        # display_message(one_a.msg)
        # choose_scene(one_a, two_a, two_b)

        scene = ConsoleWriter()
        scene.write(one_a.msg)
        scene.write(one_a.image, effect=False)
        get_user_input("Choose 1 or 2: ")
        scene.clear()
        scene.write(two_a.msg)
