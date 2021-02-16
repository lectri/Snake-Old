import pyglet
import game
from pyglet.window import key
from main_window import Window
from game import Player, Apple, Checks

# Create Instance
window = Window()
player = Player()
apple = Apple()
checks = Checks()

# Create Window
window.create_window()


@window.instance.event
def on_draw():
    window.instance.clear()
    player.sprite.draw()
    window.scoreLabel.draw()


@window.instance.event
def on_key_press(symbol, modifiers):
    # Player Movement
    if symbol == key.UP:
        game.player_direction = "U"
    elif symbol == key.DOWN:
        game.player_direction = "D"
    elif symbol == key.LEFT:
        game.player_direction = "L"
    elif symbol == key.RIGHT:
        game.player_direction = "R"


# Events that should be ran multiple times a second
pyglet.clock.schedule_interval_soft(player.move, 1 / 30)

# Runs Code 
pyglet.app.run()
