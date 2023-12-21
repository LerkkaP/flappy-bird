import pygame

class Text:
    """Class to handle text attributes and collisions"""

    def __init__(self, screen_width):
        """Initialize button attributes"""
        self._screen_width = screen_width
        self._init_font()
        self._init_colors()

    def _init_font(self):
        """Set a new font"""
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def _init_colors(self):
        """Initialize colors"""
        self.text_color = (255, 255, 255)
        self.button_background_color = (255, 153, 51)

    def end_score(self, text):
        """Renders end screen scores"""
        text_render = self.font.render(text, True, self.text_color)
        text_rect = text_render.get_rect()
        if text == "SCORE":
            text_rect.center = (self._screen_width / 2, 150)
        else:
            text_rect.center = (self._screen_width / 2, 250)
        return text_render, text_rect
    
    def end_buttons(self, text):
        """Handles button text and rect"""
        text_render = self.font.render(text, True, self.text_color, self.button_background_color)
        text_rect = text_render.get_rect()
        text_rect.y = 420

        if text == 'STATS':
            text_rect.left = self._screen_width / 2 + 10
        else:
            text_rect.right = self._screen_width / 2 - 10
        return text_render, text_rect
    
    def back_button(self):
        """Handles back button text and rect"""
        text_render = self.font.render('BACK', True, self.text_color, self.button_background_color)
        text_rect = text_render.get_rect()
        text_rect.center = (self._screen_width / 2, 550)
        return text_render, text_rect        

    def check_collision(self, text_rect, mouse_pos):
        """Check if button is clicked"""
        return text_rect.collidepoint(mouse_pos)