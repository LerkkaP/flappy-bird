from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score
from utils.text import Text


class End:
    """Class for managing the end phase of the game

    Attributes:
        _screen_width: Width of the sceen
        score: Instance of score class
        text: Instance of text class
        restart_text: Surface for the restart button text
        stats_text:  Surface for the stats button text
        end_message: Game over image
        end_message_x: X-coordinate of the end message
        end_message_y: Y-coordinate of the end message
    """

    def __init__(self, screen_width):
        """Initialize end phase

        Args:
            screen_width (_type_): _description_
        """
        self._screen_width = screen_width
        self.score = Score()
        self.text = Text(screen_width)
        self.restart_text = self.text.end_buttons('RESTART')
        self.stats_text = self.text.end_buttons('STATS')

        self._init_end_message()

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
            mouse_pos: A tuple containing the x and y coordinates of the mouse click

        Returns:
            True if the mouse click was on the restart button, False otherwise
        """
        restart_text_render, restart_text_rect = self.text.end_buttons(
            'RESTART')
        return self.text.check_collision(restart_text_rect, mouse_pos)

    def handle_statistics_click(self, mouse_pos):
        """Handles the clicking of the stats button

        Args:
            mouse_pos: A tuple containing the x and y coordinates of the mouse click

        Returns:
            True if the mouse click was on the stats button, False otherwise
        """
        stats_text_render, stats_text_rect = self.text.end_buttons('STATS')
        return self.text.check_collision(stats_text_rect, mouse_pos)

    def save_score_to_database(self):
        """Saves score to database
        """
        current_score = self.score.get_score()
        save_score(current_score)
