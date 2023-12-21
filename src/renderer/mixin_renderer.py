from utils.asset_loader import AssetLoader
from utils.score import Score


class RendererMixin:
    def __init__(self):
        self.score = Score()

    def render_pipes(self, pipes, display):
        pipes.draw(display)

    def render_ground(self, ground, display):
        ground.draw(display)

    def render_bird(self, bird, display):
        bird.draw(display)

    def render_score(self, score, display, screen_width, y):
        score_digits = list(str(score))
        width = len(score_digits) * 21
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            display.blit(
                image,
                ((screen_width - width) // 2 + i * 21, y))
