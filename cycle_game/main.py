import os
import random
import pyray

# Casting Classes
from game.casting.actor import Actor
from game.casting.cast import Cast

# Director Classes
from game.directing.director import Director

# Service Classes
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

# Shared Classes
from game.shared.point import Point
from game.shared.color import Color

# Basic values for game data
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(5, 10)

def main():
    cast = Cast()

    # Create Players Information
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    # Create player 1
    cast.add_actor("player1", player)
    # Create Player 2
    cast.add_actor("player2", player)

    # Initialize Video Service
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()



