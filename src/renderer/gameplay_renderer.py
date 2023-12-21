from utils.score import Score
from .mixin_renderer import RendererMixin


class GameplayRenderer(RendererMixin):
    """Class for rendering the gameplay phase

    Args:
        RendererMixin: Mixin class RendererMixin to access common rendering functionalities

    Attributes:
        _display: Pygame display surface
        _screen_width: Width of the screen
        _game_manager: Instance of GameManager class
        score: Instance of Score class
    """

    def __init__(self, display, screen_width, game_manager):
        """Initializes GameplayRenderer class

        Args:
            display: Pygame display surface
            screen_width: Width of the screen
            game_manager: GameManager class
        """
        super().__init__()
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.score = Score()

    def render_gameplay(self):
        """Renders gameplay screen
        """
        self.render_pipes(self._game_manager.get_pipes(), self._display)
        self.render_ground(self._game_manager.get_ground(), self._display)
        self.render_bird(self._game_manager.get_bird(), self._display)
        self.render_score(self.score.get_score(),
                          self._display, self._screen_width, 50)
