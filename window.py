import pyglet

class Window:
    def __init__(self):
        # Window Information
        self.width = 480
        self.height = 360
        self.dimensions = [self.width, self.height]
        self.center = [self.width / 2, self.height]
        self.caption = "Snake"

        # Window is created
        self.window = pyglet.window.Window(self.width, self.height, caption=self.caption)

class Events:
    pass



    


