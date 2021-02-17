import pyglet


class Properties:
    def __init__(self):
        self.spriteBatch = pyglet.graphics.Batch()
        self.score = 0
        
        # Labels 
        self.scoreLabel = pyglet.text.Label(
            f"Score: {self.score}",
            font_name="Arial",
            font_size=20,
            x=0, y=0)
