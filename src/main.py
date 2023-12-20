import pygame
from game_manager import GameManager
from utils.asset_loader import AssetLoader
from renderer.base_renderer import BaseRenderer

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
icon = AssetLoader().load_image("icon", "favicon.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption('Flappy Bird')

game_manager = GameManager(screen_width, screen_height)
renderer = BaseRenderer(display, screen_width, screen_height, game_manager)

while True:
    game_manager.handle_events()
    game_manager.handle_game_state()
    renderer.render_game()
    pygame.display.update()
    clock.tick(60)
