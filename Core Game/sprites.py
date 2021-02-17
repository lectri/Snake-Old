import pyglet
from pyglet import shapes
from pyglet.window import key
from window import Window
from game import Properties


class Player(Properties):
    def __init__(self):
        super().__init__()
        # Sprite
        self.sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(0, 255, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2
        self.length = 1
        
        # Snake Properties
        self.speed = 5
        self.direction = ""
    
    def move(self, dt):
        if self.direction == "U":
            self.sprite.y += self.speed
        elif self.direction == "D":
            self.sprite.y -= self.speed
        elif self.direction == "L":
            self.sprite.x -= self.speed
        elif self.direction == "R":
            self.sprite.x += self.speed

    def grow(self):
        if self.length > 1:
            pass
        # Creates body 
        else:
            pass


class Apple(Properties):
    def __init__(self):
        super().__init__()
        '''
        self.sprite = shapes.Rectangle(x=500, y=500, width=25, height=25, color=(255, 0, 0), batch=self.spriteBatch)
        self.sprite.anchor_x = self.sprite.x // 2
        self.sprite.anchor_y = self.sprite.y // 2
        '''


