import pygame
from game_manager import GameManager
from utils.asset_loader import AssetLoader
from renderer.base_renderer import BaseRenderer


def initialize_game():
    """Initialize game components

    Returns:
        Clock, game_manager and renderer to be used in the main loop
    """

    pygame.init()
    screen_width, screen_height = 480, 620
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    icon = AssetLoader().load_image("icon", "favicon.ico")
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Flappy Bird')

    game_manager = GameManager(screen_width, screen_height)
    renderer = BaseRenderer(display, screen_width, screen_height, game_manager)

    return clock, game_manager, renderer


def run_game():
    """Main loop responsible for running the game
    """
    clock, game_manager, renderer = initialize_game()

    while True:
        game_manager.handle_events()
        game_manager.handle_game_state()
        renderer.render_game()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
