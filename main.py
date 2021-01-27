import pyglet
from pyglet.window import key
from main_window import Window
from game import Game, Snake

# Create Instance
window = Window()
game = Game()
snake = Snake()

# Game events
@window.instance.event
def on_draw():
    window.instance.clear()
    snake.body.draw()
    game.scoreLabel.draw()
@window.instance.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        snake.body.x += 5

# Runs Code 
pyglet.app.run()
