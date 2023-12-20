import pygame

class Button:
    """Class to handle button attributes and collisions"""

    def __init__(self, text, position, screen_width):
        """Initialize button attributes"""
        self._init_font()
        self._init_colors()
        self.text_render = self.font.render(
            text, True, self.button_text_color, self.button_background_color)
        self.text_rect = self.text_render.get_rect()

        if position == 'left':
            self.text_rect.left = screen_width / 2 + 10
        elif position == 'right':
            self.text_rect.right = screen_width / 2 - 10
        else:
            self.text_rect.centerx = screen_width / 2

        self.text_rect.y = 620 - 200

    def _init_font(self):
        """Set a new font"""
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def _init_colors(self):
        """Initialize colors"""
        self.button_text_color = (255, 255, 255)
        self.button_background_color = (255, 153, 51)

    def check_collision(self, mouse_pos):
        """Check if button is clicked"""
        return self.text_rect.collidepoint(mouse_pos)