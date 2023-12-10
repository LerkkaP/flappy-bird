import pygame
from renderer import Renderer
from game_manager import GameManager
from utils.asset_loader import AssetLoader

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# set PyGame icon
icon = AssetLoader().load_image("icon", "favicon.ico")
pygame.display.set_icon(icon) 
# set PyGame window caption
pygame.display.set_caption('Flappy Bird')

game_manager = GameManager(screen_width, screen_height)
renderer = Renderer(display, screen_width, screen_height, game_manager)


while True:
    game_manager.handle_events()
    game_manager.handle_game_state()
    renderer.render_background()
    renderer.render_phase()

    pygame.display.update()
    clock.tick(60)
