import pyglet
from pyglet import shapes
from pyglet.window import key
from main_window import Window

player_direction = ""


class Player(Window):
    def __init__(self):
        super().__init__()

        self.sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(0, 255, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2
        self.body = ["O"]

    def grow(self):
        # Create Body
        pass

    def move(self, dt):
        if player_direction == "U":
            self.sprite.y += 5
        elif player_direction == "D":
            self.sprite.y -= 5
        elif player_direction == "L":
            self.sprite.x -= 5
        elif player_direction == "R":
            self.sprite.x += 5


class Apple(Window):
    def __init__(self):
        super().__init__()

        self.sprite = shapes.Rectangle(x=500, y=500, width=25, height=25, color=(255, 0, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2


class Checks(Player, Window):
    def __init__(self):
        super().__init__()

    def out_of_bounds(self, dt):
        pass
