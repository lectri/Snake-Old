import pyglet
from main_window import Window
from pyglet import shapes


class Snake(Window):
    def __init__(self):
        super(Window, self).__init__()

        self.sprite = shapes.Rectangle(x=200,y=200, width=25,height=25, color=(0,255,0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2

    def move(self, dt):
        self.sprite.x += 5

    def turn(self):
        pass

    def grow(self):
        self.body.width += 10


class Apple(Window):
    def __init__(self):
        super(Apple, self).__init__()
        self.sprite = shapes.Rectangle(x=500, y=500, width=25, height=25, color=(255,0,0), batch=Window.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2


class Checks(Snake):
    def __init__(self):
        super(Checks, self).__init__
    def out_of_bounds(self, dt):
        if self.sprite.x > self.width:
            self.sprite.x = -10
        

        
        