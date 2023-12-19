import pygame
from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score

class Button:
    """Class to handle button attributes and collisions"""

    def __init__(self, text, position, screen_width):
        """Initialize button attributes"""
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.text_render = self.font.render(
            text, True, (255, 255, 255), (255, 153, 51))
        self.text_rect = self.text_render.get_rect()

        if position == 'left':
            self.text_rect.left = screen_width / 2 + 10
        else:
            self.text_rect.right = screen_width / 2 - 10

        self.text_rect.y = 620 - 200

    def check_collision(self, mouse_pos):
        """Check if button is clicked"""
        return self.text_rect.collidepoint(mouse_pos)