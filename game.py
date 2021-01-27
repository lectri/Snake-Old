import pyglet
from main_window import Window
from pyglet import shapes


class Game(Window):
    def __init__(self):
        # Gives me all the stuff from the Window class
        super(Window,self).__init__()
        # The snake square itself
        
        self.score = 0
        self.spriteBatch = pyglet.graphics.Batch()
        self.scoreLabel = pyglet.text.Label(
            f"Score:{self.score}",
            font_name="Arial",
            font_size=20,
            x=0,y=0
        )


class Snake(Game):
    def __init__(self):
        super().__init__()
        
        self.body = shapes.Rectangle(x=200,y=200, width=25,height=25, color=(0,255,0), batch=self.spriteBatch)
        self.body.anchor_x = self.body.x // 2
        self.body.anchor_y = self.body.y // 2
    
    def turn(self):
        pass

    def grow(self):
        self.body.width += 5


class Apple:
    pass


            
        

        
        