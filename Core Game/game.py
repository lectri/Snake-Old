import pyglet
from main_window import Window
from pyglet import shapes


class Snake(Window):
    def __init__(self):
        super().__init__()

        self.sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(0, 255, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2
        self.direction = "North"

    def move(self, dt, direction):
        if direction == "North":
            self.sprite.y += 5
        elif direction == "South":
            self.sprite.y -= 5
        elif direction == "East":
            self.sprite.x += 5
        elif direction == "West":
            self.sprite.x -= 5
        else:
            return "Invalid Direction"


    def grow(self):
        self.body.width += 10



class Apple(Window):
    def __init__(self):
        super().__init__()

        self.sprite = shapes.Rectangle(x=500, y=500, width=25, height=25, color=(255, 0, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2


class Checks(Snake, Window):
    def __init__(self):
        super().__init__()

    def out_of_bounds(self, dt):
        if self.sprite.x > self.width:
            self.sprite.position = -10
