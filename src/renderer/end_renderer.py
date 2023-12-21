from utils.score import Score
from utils.text import Text
from db.database_actions import get_highest_score
from .mixin_renderer import RendererMixin


class EndRenderer(RendererMixin):
    """Class for rendering the end phase

    Args:
        RendererMixin: Mixin class RendererMixin to access common rendering functionalities

    Attributes:
        _display: Pygame display surface
        _screen_width: Width of the screen
        _game_manager: Instance of GameManager class
        text: Instance of Text class
        score: Instance of Score class
    """

    def __init__(self, display, screen_width, game_manager):
        """Initializes EndRenderer class

        Args:
            display: Pygame display surface
            screen_width: Width of the screen
            game_manager: GameManager class
        """
        super().__init__()
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.text = Text(screen_width)
        self.score = Score()

    def render_end(self):
        """Renders end screen
        """
        self.render_pipes(self._game_manager.get_pipes(), self._display)
        self.render_ground(self._game_manager.get_ground(), self._display)
        self.render_bird(self._game_manager.get_bird(), self._display)
        self._render_game_over()
        self._render_end_scores()
        self._render_buttons()

    def _render_game_over(self):
        """Renders game over image
        """
        end_message, end_message_coordinates = self._game_manager.get_end_message()
        self._display.blit(end_message, end_message_coordinates)

    def _render_end_scores(self):
        """Renders end scores
        """
        self._render_end_score("SCORE", y=170)
        self._render_end_score("BEST", y=270)

    def _render_end_score(self, score_type, y):
        """Renders current gameplay session score

        Args:
            score_type: Type of score to be rendered either SCORE or BEST 
            y: Y-location on the screen where the score is blit
        """
        score_text_render, score_text_rect = self.text.end_score(score_type)
        self._display.blit(score_text_render, score_text_rect)
        score_value = self.score.get_score() if score_type == "SCORE" else get_highest_score()
        self.render_score(score_value, self._display, self._screen_width, y)

    def _render_buttons(self):
        """Renders buttons RESTART AND STATS
        """
        restart_text_render, restart_text_rect = self.text.end_buttons(
            'RESTART')
        stats_text_render, stats_text_rect = self.text.end_buttons('STATS')

        self._display.blit(restart_text_render, restart_text_rect)
        self._display.blit(stats_text_render, stats_text_rect)
