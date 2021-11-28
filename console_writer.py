import os
import platform
import sys
from time import sleep

from playsound import playsound


class ConsoleWriter:
    def clear(self):
        """Clears the console of any text on Windows, Mac, and Linux."""
        _os = platform.system()
        return os.system("cls") if _os == "Windows" else os.system("clear")

    def set_char_print_speed(self, char):
        """Hacky way of trying to detect end of a sentence and 'pause' longer there
        so the user has more time to read before the next sentence starts."""
        return sleep(3) if char == "." else sleep(0.04)

    def start_typing_effect(self, msg):
        """Prints each char out and sleeps x amount of time before printing the next char.
        This produces visual typing effect."""
        for char in msg:
            self.set_char_print_speed(char)
            sys.stdout.write(char)
            sys.stdout.flush()

    def write(self, msg, sound="audio/writing.wav", effect=True):
        """Takes a message and a sound. Plays the sound and then displays
        the message with the type writer effect if effect is set to True (default)."""
        playsound(sound, False)
        if effect:
            self.start_typing_effect(msg)
        else:
            sys.stdout.write(msg)
