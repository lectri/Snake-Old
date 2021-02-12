import pyglet
from pyglet.window import key
from main_window import Window
from game import Snake, Apple, Checks

# Create Instance
window = Window()
snake = Snake()
apple = Apple()
checks = Checks()

# Create Window 
window.create_window()

# Input-Dependent Events
@window.instance.event
def on_draw():
    window.instance.clear()
    snake.sprite.draw()
    window.scoreLabel.draw()
@window.instance.event
def on_key_press(symbol, modifiers):
    pass

# Time-Dependent Events
pyglet.clock.schedule_interval(snake.move, 1/30) 
pyglet.clock.schedule_interval(checks.out_of_bounds, 1/30)
# Runs Code 
pyglet.app.run()
