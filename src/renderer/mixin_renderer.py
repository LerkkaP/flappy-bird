from utils.asset_loader import AssetLoader
from utils.score import Score


class RendererMixin:
    """Mixin class that holds common rendering functionality

    Attributes:
        score: Instance of Score class
    """

    def __init__(self):
        """Initialize RendererMixin class"""
        self.score = Score()

    def render_pipes(self, pipes, display):
        """Renders pipes

        Args:
            pipes: Pygame group of pipe objects
            display: Pygame display surface
        """
        pipes.draw(display)

    def render_ground(self, ground, display):
        """Renders ground

        Args:
            ground: Pygame group of ground objects
            display: Pygame display surface
        """
        ground.draw(display)

    def render_bird(self, bird, display):
        """Renders bird

        Args:
            bird: Pygame group of bird objects
            display: Pygame display surface
        """
        bird.draw(display)

    def render_score(self, score, display, screen_width, y):
        """Renders score

        Args:
            score: Score to be displayed
            display: Pygame display surface
            screen_width: Width of the screen
            y: Y-location on the screen where the score is blit
        """
        score_digits = list(str(score))
        width = len(score_digits) * 21
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            display.blit(
                image,
                ((screen_width - width) // 2 + i * 21, y))
