from time import sleep
from console_writer import ConsoleWriter as console


class SceneController:
    """Controls how and when each scene get's played based on user input."""
    def validate_user_input(self,game_control, prompt='Choose 1 or 2: '):
        """ Checks if user input is equal to a game_control.
        Used to determine which scene to que next. """
        while True:
            try:
                choice = str(input(prompt))
            except ValueError:
                print("Oops looks like you fat-fingered it, try '1' or '2'.")
                continue
            else:
                break
        if choice == game_control:
            return True
        return False

    def que_next_scene(self, current_scene, next_scene_a, next_scene_b):
        choices = {
            "a": {
                "choice": current_scene.choices["a"]["choice"],
                "img": current_scene.choices["a"]["img"],
            },
            "b": {
                "choice": current_scene.choices["b"]["choice"],
                "img": current_scene.choices["b"]["img"],
            },
        }

        if self.validate_user_input("a"):
            selected_choice = choices.a.choice
            console.write(selected_choice)
            sleep(2)
            console.clear()
            console.write(next_scene_a.img, False)
            console.write(next_scene_a.msg)
        elif self.validate_user_input("b"):
            selected_choice = choices.b.choice
            console.write(selected_choice)
            sleep(2)
            console.clear()
            console.write(next_scene_b.img, False)
            console.write(next_scene_b.msg)
        else:
            "Please enter a valid choice, 1 or 2"
            self.que_next_scene(current_scene, next_scene_a, next_scene_b)
