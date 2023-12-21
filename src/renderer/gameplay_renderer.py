from utils.score import Score
from .mixin_renderer import RendererMixin


class GameplayRenderer(RendererMixin):
    def __init__(self, display, screen_width, game_manager):
        super().__init__()
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.score = Score()

    def render_gameplay(self):
        self.render_pipes(self._game_manager.get_pipes(), self._display)
        self.render_ground(self._game_manager.get_ground(), self._display)
        self.render_bird(self._game_manager.get_bird(), self._display)
        self.render_score(self.score.get_score(),
                          self._display, self._screen_width, 50)
