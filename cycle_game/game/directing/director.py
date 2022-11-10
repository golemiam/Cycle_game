from game.shared.point import Point
#from game.casting.artifact import Artifact
#from game.shared.color import Color
import random

# Basic values for game data
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40

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
        self.player_score = 0
        
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


    








    


    