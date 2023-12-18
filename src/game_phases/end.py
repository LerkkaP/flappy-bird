import pygame
from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score, get_highest_score


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

        self._init_end_message()
        self._init_restart_button()
        self._init_statistics_button()

    def _init_restart_button(self):
        """Initialize restart button attributes
        """
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.restart_text = self.font.render(
            'RESTART', True, (255, 255, 255), (255, 153, 51))
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.right = (self._screen_width / 2) - 10
        self.restart_text_rect.y = 620 - 200

    def _init_statistics_button(self):
        """Initialize statistics button attributes
        """
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.statistics_text = self.font.render(
            'STATS', True, (255, 255, 255), (255, 153, 51))
        self.statistics_text_rect = self.statistics_text.get_rect()
        self.statistics_text_rect.left = self._screen_width / 2 + 10
        self.statistics_text_rect.y = 620 - 200

    def _init_end_message(self):
        """Initialize end message attributes
        """
        self.end_message = AssetLoader.load_image("messages", "end.png")
        self.end_message_x = (
            self._screen_width - self.end_message.get_width()) // 2

        self.end_message_y = 50

    def handle_restart_click(self, mouse_pos):
        """Handles the clicking of the restart button

        Args:
            mouse_pos: Cursor position

        Returns:
            bool: True if cursor position collides with the restart text, else False
        """
        if self.restart_text_rect.collidepoint(mouse_pos):
            return True
        return False
    
    def handle_statistics_click(self, mouse_pos):
        """Handles the clicking of the figures button

        Args:
            mouse_pos: Cursor position

        Returns:
            bool: True if cursor position collides with the figures text, else False
        """
        if self.statistics_text_rect.collidepoint(mouse_pos):
            return True
        return False
    
    def save_score_to_database(self):
        """Saves score to database
        """
        current_score = self.score.get_score()
        save_score(current_score)

    def get_highest_score_from_database(self):
        """Retrieves highest score from database
        """
        get_highest_score()
