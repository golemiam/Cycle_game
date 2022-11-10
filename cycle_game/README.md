Requirements:
    The program must include a README file.
    The program must include class and method comments.
    The program must have at least 16 classes.
    The program must remain true to game play described in the overview.
# CSE210-05: Cycle Game

# TODO 
    

## Overview: 
    Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

    Rules:
        Players can move in all cardinal directions.
            Player one moves using the W, S, A and D keys.
            Player two moves using the I, K, J and L keys.
        Each player's trail grows as they move.
        Players try to maneuver so the opponent collides with their trail.
        If a player collides with their opponent's trail
            A "game over" message is displayed in the middle of the screen
            The cycle turns white
            Players keep moving and turning but don't run into each other.

## Running the Game:
To start the game, begin by running the "__main__.py" file. 

## Help/Information:
    There is a lot from this program that borrows similar elements already created for us in the rfk activity from the BYUI week07 activity, so to save time and help ensure quality, those essential components have been included.

    Directory is as follows:
    root                                 (project root folder)
    |
    \-- cycle_game                       (source code for game)
    |   |
    |   \-- game                         (specific game classes)
    |   |   |
    |   |   \-- casting                  (contains casting classes)
    |   |   |   |
    |   |   |   \-- actor.py
    |   |   |   \-- cast.py
    |   |   |
    |   |   \-- directing                (contains director class)
    |   |   |   |
    |   |   |   \-- director.py
    |   |   |
    |   |   \-- services                 (contains service classes)
    |   |   |   |
    |   |   |   \-- keyboard_service.py  (borrowed from BYUI: week07 rfk activity)
    |   |   |   \-- video_service.py     (borrowed from BYUI: week07 rfk activity)
    |   |   |
    |   |   \-- shared                   (contains shared classes)
    |   |       |
    |   |       \-- color.py             (borrowed from BYUI: week07 rfk activity)
    |   |       \-- point.py             (borrowed from BYUI: week07 rfk activity)
    |   |
    |   \-- __main__.py                  (entry point for program)
    |
    \-- README.md                        (general info)

    To find more information, you can see the base code in the repository at https://
    rfk files borrowed from activity located at https://byui-cse.github.io/cse210-course-competency/inheritance/materials/rfk-specification.html

## Contributers:
    Helaman Cristian Pinheiro Ewerton - 
    Lorenzo Tarati - 
    Marc Rollins - 
    Robbie Platt - 
