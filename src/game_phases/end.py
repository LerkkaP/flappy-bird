from utils.asset_loader import AssetLoader
from utils.score import Score
from db.database_actions import save_score, get_highest_score


class End:
    def __init__(self, screen_width):
        self._screen_width = screen_width
        self.score = Score()

        self._init_end_message()

    def _init_end_message(self):
        self.end_message = AssetLoader.load_image("messages", "end.png")
        self.end_message_x = (
            self._screen_width - self.end_message.get_width()) // 2
        
        self.end_message_y = 150
        
    def save_score_to_database(self):
        current_score = self.score.get_score()
        save_score(current_score)

    def get_highest_score_from_database(self):
        get_highest_score()



