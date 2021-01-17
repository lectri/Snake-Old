import pyglet
from main_window import Window
from game import Game

w = Window()
g = Game()


# Handles game events (drawing, keyboard presses, etc.)
@w.mainWindow.event
def on_draw():
    w.mainWindow.clear()
    g.snake.draw()
    g.scoreLabel.draw()


pyglet.app.run()
    