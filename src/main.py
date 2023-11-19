import pygame
import os
from start import Start
from gameplay import Gameplay

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 620
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()        

dirname = os.path.dirname(__file__)

background_image = pygame.image.load(os.path.join(dirname, "assets/images/world", "background-day.png"))
background_image = pygame.transform.scale(background_image,(SCREEN_WIDTH, SCREEN_HEIGHT))

start_message = pygame.image.load(os.path.join(dirname, "assets/images/messages", "start.png"))
start_message_x = (SCREEN_WIDTH - start_message.get_width()) // 2
start_message_y = (SCREEN_HEIGHT - start_message.get_height()) // 2

start_phase = Start(SCREEN_WIDTH, SCREEN_HEIGHT)
gameplay_phase = Gameplay(SCREEN_WIDTH, SCREEN_HEIGHT)

hover_speed = 0.25
hover_range = 5
hover_direction = 1  
current_hover = 0  

game_phase = "start"

while True:
    display.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_phase = "gameplay" 
                gameplay_phase.fly(0, -50)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_phase = "gameplay"
            gameplay_phase.fly(0, -50)

    if game_phase == "start":

        start_phase.ground.draw(display)
        start_phase.ground.update()
        start_phase.update_ground()

        current_hover += hover_speed * hover_direction
        if abs(current_hover) >= hover_range:
            hover_direction *= -1

        hover_offset_y = start_message_y + current_hover
        display.blit(start_message, (start_message_x, hover_offset_y))

    elif game_phase == "gameplay":

        gameplay_phase.start_phase.ground.draw(display)
        gameplay_phase.start_phase.ground.update()
        gameplay_phase.start_phase.update_ground()

        gameplay_phase.bird.draw(display)
        gameplay_phase.bird.update()
        if not any(pygame.key.get_pressed()):
            gameplay_phase.fall()
        

    pygame.display.update()
    clock.tick(60)
