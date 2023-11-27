import pygame
from game_manager import GameManager

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game_manager = GameManager(screen_width, screen_height)

while True:
    game_manager.handle_events()
    game_manager.handle_game_state()
    game_manager.render(display)

    pygame.display.update()
    clock.tick(60)
