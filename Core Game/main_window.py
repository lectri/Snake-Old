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
        self.caption = "Player"
        self.spriteBatch = pyglet.graphics.Batch()

        # Labels
        self.score = 0
        self.scoreLabel = pyglet.text.Label(
            f"Score: {self.score}",
            font_name="Arial",
            font_size=20,
            x=0, y=0)

    def create_window(self):
        # Putting this in the init will cause child classes to make multiple windows.
        self.instance = pyglet.window.Window(self.width, self.height, caption=self.caption)
