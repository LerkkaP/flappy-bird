from utils.asset_loader import AssetLoader
from utils.score import Score


class GameplayRenderer():
    def __init__(self, display, screen_width, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.score = Score()

    def render_gameplay(self):
        self._render_pipes()
        self._render_ground()
        self._render_bird()
        self._render_score(50)

    def _render_pipes(self):
        self._game_manager.gameplay_phase.pipe_movement.pipe.draw(
            self._display)
        
    def _render_ground(self):
        self._game_manager.gameplay_phase.ground_movement.ground.draw(
                self._display)
        
    def _render_bird(self):
        self._game_manager.gameplay_phase.bird.draw(self._display)

    def _render_score(self, y):
        score = self.score.get_score()
        score_digits = list(str(score))
        width = len(score_digits) * 21
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - width) // 2 + i * 21, y))