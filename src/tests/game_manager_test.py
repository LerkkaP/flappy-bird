import unittest
from unittest.mock import MagicMock
from game_manager import GameManager

screen_width = 480
screen_height = 620

class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.game_manager = GameManager(screen_width, screen_height)

        self.mock_start_phase = MagicMock()
        self.mock_gameplay_phase = MagicMock()
        self.mock_phase_manager = MagicMock()
        
        self.game_manager.start_phase = self.mock_start_phase
        self.game_manager._gameplay_phase = self.mock_gameplay_phase
        self.game_manager._phase_manager = self.mock_phase_manager

    def test_that_handle_game_state_calls_correct_methods_in_start(self):
        self.mock_phase_manager.game_in_start.return_value = True
        self.game_manager.handle_game_state()

        self.mock_start_phase.update.assert_called_once()
        self.mock_start_phase.handle_text_hover.assert_called_once()


