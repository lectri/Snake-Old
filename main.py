import pyglet
from pyglet.window import key
from main_window import Window
from game import Game, Snake


window = Window()
game = Game()
snake = Snake()

# Handles game events (drawing, keyboard presses, etc.)
@window.instance.event
def on_draw():
    window.instance.clear()
    snake.body.draw()
    game.scoreLabel.draw()

def on_key_press(symbol, modifiers):
    pass


pyglet.app.run()
