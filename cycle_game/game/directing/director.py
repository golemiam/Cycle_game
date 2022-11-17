from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color
import random

# Basic values for game data
CELL_SIZE = 15
FONT_SIZE = 30
COLS = 60
ROWS = 40
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)

class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.player1_score = 0
        self.player2_score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        player1 = cast.get_first_actor("player1")
        p1_velocity = self._keyboard_service.get_player1_direction()
        player1.set_velocity(p1_velocity)

        player2 = cast.get_first_actor("player2")
        p2_velocity = self._keyboard_service.get_player2_direction()
        player2.set_velocity(p2_velocity)
    
    def _do_updates(self, cast):
        """Updates the position's position and resolves any collisions with players/their trails.

        Args:
            cast (Cast): The cast of actors.
        """
        # Retrieve actor data
        p1_banner = cast.get_first_actor("p1_banner")
        p2_banner = cast.get_first_actor("p2_banner")
        player1 = cast.get_first_actor("player1")
        p1_position = player1.get_position()
        player2 = cast.get_first_actor("player2")
        p2_position = player2.get_position()

        # Create barriers
        p1_barrier = Actor()
        p1_barrier.set_text("#")
        p1_barrier.set_font_size(FONT_SIZE)
        p1_barrier.set_color(RED)
        p1_barrier.set_position(p1_position)
        cast.add_actor("p1_barriers", p1_barrier)

        p2_barrier = Actor()
        p2_barrier.set_text("#")
        p2_barrier.set_font_size(FONT_SIZE)
        p2_barrier.set_color(BLUE)
        p2_barrier.set_position(p2_position)
        cast.add_actor("p2_barriers", p2_barrier)

        # Update player scores and positions
        p1_banner.set_text(f"P1 Score: {self.player1_score}")
        p2_banner.set_text(f"P2 Score: {self.player2_score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player1.move_next(max_x, max_y)
        player2.move_next(max_x, max_y)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()