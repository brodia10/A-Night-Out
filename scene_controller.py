from console_writer import ConsoleWriter

console = ConsoleWriter()


class SceneController:
    """
    This Class defines methods for determining:
        - when and how to start a scene
        - which scene should be played next based off of user input
    """

    def user_input_is_valid(self, prompt=""):
        """ Checks that user input matches game controls: 1 or 2. Optionally displays a prompt."""
        while True:
            try:
                user_input = input(prompt)
                if user_input == "1" or user_input == "2":
                    return user_input
            except ValueError as e:
                print(e)
                continue

    def start(self, current_scene, next_scene_a, next_scene_b):
        """Takes the current scene, and the two possible next scenes. Starts the next scene based on user input. """
        # TODO: add audio parameter for playing the scene's theme music

        # Map choices to scene choices
        choice_a = current_scene.choices["a"]
        choice_b = current_scene.choices["b"]

        # Play current scene
        console.write(current_scene.msg)
        console.write(current_scene.img, effect=False)

        # Display prompt and validate user input
        input = self.user_input_is_valid(
            f"""[1] {choice_a['choice']} \n[2] {choice_b['choice']} \nJake chooses: """
        )

        # Play next scene msg and img based on user input.
        if input == "1":
            console.write(choice_a["img"], effect=False)
            console.write(choice_a["choice"])
            console.clear()
            console.write(next_scene_a.msg)
        else:
            console.write(choice_b["img"], effect=False)
            console.write(choice_b["choice"])
            console.clear()
            console.write(next_scene_b.msg)
