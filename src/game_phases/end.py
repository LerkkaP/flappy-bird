import pygame
from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score, get_highest_score
from utils.button import Button


class End:
    """Class for managing the end phase of the game

    Attributes:
        _screen_width: Width of the sceen
        score: Instance of score class
        _init_end_message: Initialization of game over message attributes
        _init_restart_button: Initialization of restart button attributes
        _init_statistics_button: Initialization of statistics button attributes

    """

    def __init__(self, screen_width):
        """Initialize end phase

        Args:
            screen_width (_type_): _description_
        """
        self._screen_width = screen_width
        self.score = Score()

        self.restart_button = Button('RESTART', 'right', self._screen_width)
        self.statistics_button = Button('STATS', 'left', self._screen_width)
        
        self._init_end_message()

    def _init_end_message(self):
        """Initialize end message attributes
        """
        self.end_message = AssetLoader.load_image("messages", "end.png")
        self.end_message_x = (
            self._screen_width - self.end_message.get_width()) // 2

        self.end_message_y = 50
    
    def handle_restart_click(self, mouse_pos):
        """Handles the clicking of the restart button"""
        return self.restart_button.check_collision(mouse_pos)

    def handle_statistics_click(self, mouse_pos):
        """Handles the clicking of the stats button"""
        return self.statistics_button.check_collision(mouse_pos)
    
    def save_score_to_database(self):
        """Saves score to database
        """
        current_score = self.score.get_score()
        save_score(current_score)
