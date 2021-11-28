class Scene(object):
    """Class definition for a scene."""
    def __init__(self, name, msg, img, choices):
        self.name = name
        self.msg = msg
        self.img = img
        self.choices = choices

    def get_choices(self):
        return self.choices

    def get_msg(self):
        return self.msg

    def get_img(self):
        return self.img

    def get_choices(self):
        return self.choices
