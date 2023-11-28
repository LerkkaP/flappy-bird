import unittest
from unittest.mock import MagicMock
from game_phases.start import Start


class TestStartPhase(unittest.TestCase):

    def setUp(self):
        self.screen_width = 480
        self.screen_height = 620

        self.start_phase = Start(self.screen_width,  self.screen_height)

        self.mock_ground_movement = MagicMock()
        self.start_phase.ground_movement = self.mock_ground_movement

    def test_start_phase_update_calls_ground_movement_methods(self):
        self.start_phase.update()

        self.mock_ground_movement.ground.update.assert_called_once()
        self.mock_ground_movement.update_ground.assert_called_once()
