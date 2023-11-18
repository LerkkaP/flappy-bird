import pygame
import os
from sprites.ground import Ground
from start import Start

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 620
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()        

dirname = os.path.dirname(__file__)

background_image = pygame.image.load(os.path.join(dirname, "assets/images/world", "background-day.png"))
background_image = pygame.transform.scale(background_image,(SCREEN_WIDTH, SCREEN_HEIGHT))

start_phase = Start(SCREEN_WIDTH)

while True:
    display.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    start_phase.ground.draw(display)
    start_phase.ground.update()
    start_phase.update_ground()
    
    pygame.display.update()
    clock.tick(60)
