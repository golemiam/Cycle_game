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
FONT_SIZE = 30
SCORE_FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Cycles"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)
DEFAULT_ARTIFACTS = random.randint(5, 10)

def main():
    # Create the cast
    cast = Cast()

    # Create the banner for player 1
    p1_banner = Actor()
    p1_banner.set_text("")
    p1_banner.set_font_size(SCORE_FONT_SIZE)
    p1_banner.set_color(WHITE)
    p1_banner.set_position(Point(CELL_SIZE, 5))
    cast.add_actor("p1_banner", p1_banner)

    # Create the banner for player 2
    p2_banner = Actor()
    p2_banner.set_text("")
    p2_banner.set_font_size(SCORE_FONT_SIZE)
    p2_banner.set_color(WHITE)
    p2_banner.set_position(Point(765, 5))
    cast.add_actor("p2_banner", p2_banner)

    # Create Player 1 Information
    x = int(MAX_X / 4)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    # Create player 1
    player1 = Actor()
    player1.set_text("@")
    player1.set_font_size(FONT_SIZE)
    player1.set_color(RED)
    player1.set_position(position)
    cast.add_actor("player1", player1)

    # Create Player 2 Information
    x = int((MAX_X / 4)*3)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    # Create Player 2
    player2 = Actor()
    player2.set_text("@")
    player2.set_font_size(FONT_SIZE)
    player2.set_color(BLUE)
    player2.set_position(position)
    cast.add_actor("player2", player2)

    # Initialize Video Service
    
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)
    
if __name__ == "__main__":
    main()



