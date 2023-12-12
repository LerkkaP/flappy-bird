import pygame
from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score, get_highest_score


class End:
    def __init__(self, screen_width):
        self._screen_width = screen_width
        self.score = Score()


        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.restart_text = self.font.render('RESTART', True, (255, 255, 255), (240, 175, 53))
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.right = (screen_width / 2) - 10
        self.restart_text_rect.y = 620 - 200

        self._init_end_message()

    def _init_end_message(self):
        self.end_message = AssetLoader.load_image("messages", "end.png")
        self.end_message_x = (
            self._screen_width - self.end_message.get_width()) // 2
        
        self.end_message_y = 150

    def handle_restart_click(self, mouse_pos):
        if self.restart_text_rect.collidepoint(mouse_pos):
            return True 
        return False 
        
    def save_score_to_database(self):
        current_score = self.score.get_score()
        save_score(current_score)

    def get_highest_score_from_database(self):
        get_highest_score()



