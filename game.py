import pyglet
from main_window import Window
from pyglet import shapes


class Game(Window):
    def __init__(self):
        # Gives me all the stuff from the Window class
        super(Window,self).__init__()
        # The snake square itself
        self.snake = shapes.Rectangle(x=200,y=200, width=200,height=200, color=(0,255,0))

        self.score = 0
        self.scoreLabel = pyglet.text.Label(
            f"Score:{self.score}",
            font_name="Arial",
            font_size=20,
            x=0,y=0)

            
        

        
        