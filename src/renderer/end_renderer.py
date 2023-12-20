from utils.score import Score
from utils.button import Button
from utils.asset_loader import AssetLoader
from db.database_actions import get_highest_score


class EndRenderer():
    def __init__(self, display, screen_width, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.score_text = Button('Score', 'center', screen_width)
        self.best_text = Button('Best', 'center', screen_width)
        self.score = Score()

    def render_end(self):
        self._render_pipes()
        self._render_ground()
        self._render_bird()
        self._render_end_message()
        self._render_end_scores()
        self._render_buttons()

    def _render_pipes(self):
        self._game_manager.gameplay_phase.pipe_movement.pipe.draw(
            self._display)
        
    def _render_ground(self):
        self._game_manager.gameplay_phase.ground_movement.ground.draw(
                self._display)
        
    def _render_bird(self):
        self._game_manager.gameplay_phase.bird.draw(self._display)

    def _render_end_message(self):
        self._display.blit(
            self._game_manager.end_phase.end_message,
            (
                self._game_manager.end_phase.end_message_x,
                self._game_manager.end_phase.end_message_y
            )
        )

    def _render_end_scores(self):
        score_text_render = self.score_text.text_render
        score_text_rect = self.score_text.text_rect
        score_text_rect.center = (self._screen_width / 2, 150)
        self._display.blit(score_text_render, score_text_rect)

        self._render_score(170)  

        best_text_render = self.best_text.text_render
        best_text_rect = self.best_text.text_rect
        best_text_rect.center = (self._screen_width / 2, 250)
        self._display.blit(best_text_render, best_text_rect)

        self._render_highest_score()  

    def _render_buttons(self):
        restart_text = self._game_manager.end_phase.restart_button.text_render
        restart_text_rect = self._game_manager.end_phase.restart_button.text_rect

        stats_text = self._game_manager.end_phase.statistics_button.text_render
        stats_text_rect = self._game_manager.end_phase.statistics_button.text_rect

        self._display.blit(restart_text, restart_text_rect)
        self._display.blit(stats_text, stats_text_rect)

    def _render_score(self, y):
        score = self.score.get_score()
        score_digits = list(str(score))
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, y))

    def _render_highest_score(self):
        highest_score = get_highest_score()
        score_digits = list(str(highest_score))
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, 270))