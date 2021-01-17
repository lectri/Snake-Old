import pyglet

class Window:
    def __init__(self):
        # Window Information
        self.width = 640
        self.height = 480
        self.dimensions = [self.width, self.height]
        self.center = [self.width // 2, self.height // 2]
        self.centerWidth = self.center[0]
        self.centerHeight = self.center[1]
        self.caption = "Snake"

        # Window is created
        self.mainWindow = pyglet.window.Window(self.width, self.height, caption=self.caption)
    




        



    


