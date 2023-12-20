from utils.score import Score
from utils.text import Text
from utils.asset_loader import AssetLoader
from db.database_actions import get_highest_score


class EndRenderer():
    def __init__(self, display, screen_width, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._game_manager = game_manager
        self.text = Text(screen_width)
        self.score = Score()

    def render_end(self):
        self._render_pipes()
        self._render_ground()
        self._render_bird()
        self._render_game_over()
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

    def _render_game_over(self):
        self._display.blit(
            self._game_manager.end_phase.end_message,
            (
                self._game_manager.end_phase.end_message_x,
                self._game_manager.end_phase.end_message_y
            )
        )

    def _render_end_scores(self):
        self._render_end_score()
        self._render_end_score_best()

    def _render_end_score(self):
        score_text_render, score_text_rect = self.text.end_score("SCORE")
        self._display.blit(score_text_render, score_text_rect)
        self._render_score(170)

    def _render_end_score_best(self):
        best_text_render, best_text_rect = self.text.end_score("BEST")
        self._display.blit(best_text_render, best_text_rect)
        self._render_highest_score(270)

    def _render_buttons(self):
        restart_text_render, restart_text_rect = self.text.end_buttons('RESTART')
        stats_text_render, stats_text_rect = self.text.end_buttons('STATS')

        self._display.blit(restart_text_render, restart_text_rect)
        self._display.blit(stats_text_render, stats_text_rect)
   
    def _render_score(self, y):
        score = self.score.get_score()
        self._render_digits(score, y)

    def _render_highest_score(self, y):
        highest_score = get_highest_score()
        self._render_digits(highest_score, y)
            
    def _render_digits(self, value, y):
        score_digits = list(str(value))
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, y))