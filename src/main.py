import pygame
import os
from game_phases.start import Start
from game_phases.gameplay import Gameplay
from ground_movement import GroundMovement

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()        

dirname = os.path.dirname(__file__)

background_image = pygame.image.load(os.path.join(dirname, "assets/images/world", "background-day.png"))
background_image = pygame.transform.scale(background_image,(screen_width, screen_height))

start_phase = Start(screen_width, screen_height)
gameplay_phase = Gameplay(screen_width, screen_height)

ground_movement = GroundMovement(screen_width, screen_height)

hover_speed = 0.25
hover_range  = 5
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
                gameplay_phase.fly(0, -20)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_phase = "gameplay"
            gameplay_phase.fly(0, -20)

    if game_phase == "start":
        ground_movement.ground.draw(display)
        ground_movement.ground.update()
        ground_movement.update_ground()

        current_hover += hover_speed * hover_direction
        if abs(current_hover) >= hover_range:
            hover_direction *= -1

        hover_offset_y = start_phase.start_message_y + current_hover
        display.blit(start_phase.start_message, (start_phase.start_message_x, hover_offset_y))        
    
    elif game_phase == "gameplay":
        ground_movement.ground.draw(display)
        ground_movement.ground.update()
        ground_movement.update_ground()

        gameplay_phase.bird.draw(display)
        gameplay_phase.bird.update()
        if not any(pygame.key.get_pressed()):
            gameplay_phase.fall()
        
        ground_collision = pygame.sprite.groupcollide(ground_movement.ground, gameplay_phase.bird, False, False)
        if ground_collision:
            pygame.quit()
            
    pygame.display.update()
    clock.tick(60)
