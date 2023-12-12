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
        self.assertEqual(self.game_manager.phase_manager.game_in_start(), True)

        key_press = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        pygame.event.post(key_press)

        self.game_manager.handle_events()

        self.assertEqual(self.game_manager.phase_manager.game_in_gameplay(), True)

    def test_start_events(self):
        click_mouse = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1})
        pygame.event.post(click_mouse)

        self.game_manager._handle_start_events(click_mouse)
        self.assertEqual(self.game_manager.phase_manager.game_in_gameplay(), True)

        click_space = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        pygame.event.post(click_space)

        self.game_manager._handle_start_events(click_space)
        self.assertEqual(self.game_manager.phase_manager.game_in_gameplay(), True)

    def test_that_game_is_restarted(self):
        self.game_manager._restart_game()
        self.assertEqual(self.game_manager.phase_manager.game_in_start(), True)
