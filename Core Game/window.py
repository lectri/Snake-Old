import pyglet


class Window:
    def __init__(self):
        # Window Information
        self.width = 640
        self.height = 480
        self.dimensions = [self.width, self.height]
        self.center = [self.width // 2, self.height // 2]
        self.caption = "Snake"
        

    def create_window(self):
        # Putting this in the init will cause child classes to make multiple windows.
        self.instance = pyglet.window.Window(self.width, self.height, caption=self.caption)
