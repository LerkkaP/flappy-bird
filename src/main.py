import pygame
from renderer import Renderer
from game_manager import GameManager

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game_manager = GameManager(screen_width, screen_height)
renderer = Renderer(display, screen_width, screen_height, game_manager)


while True:
    game_manager.handle_events()
    game_manager.handle_game_state()
    renderer.render_background()
    renderer.render_phase()

    pygame.display.update()
    clock.tick(60)
