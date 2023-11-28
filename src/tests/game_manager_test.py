import pygame
import unittest
from game_manager import GameManager


class TestGameManager(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen_width = 480
        self.screen_height = 620
        self.game_manager = GameManager(self.screen_width, self.screen_height)

    def test_that_initial_game_phase_is_start_and_after_key_press_gameplay(self):
        self.assertEqual(self.game_manager.game_phase, "start")

        key_press = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        pygame.event.post(key_press)

        self.game_manager.handle_events()

        self.assertEqual(self.game_manager.game_phase, "gameplay")
