import pygame
from game_phases.start import Start
from game_phases.gameplay import Gameplay
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.asset_loader import AssetLoader

pygame.init()
screen_width, screen_height = 480, 620
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()        

background_image = AssetLoader.load_image("world", "background-day.png")
background_image = pygame.transform.scale(background_image,(screen_width, screen_height))

start_phase = Start(screen_width, screen_height)
gameplay_phase = Gameplay(screen_width, screen_height)
ground_movement = GroundMovement(screen_width, screen_height)
pipe_movement = PipeMovement(screen_width, screen_height)

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
        start_phase.update()
        start_phase.render(display)

        current_hover += hover_speed * hover_direction
        if abs(current_hover) >= hover_range:
            hover_direction *= -1

        hover_offset_y = start_phase.start_message_y + current_hover
        display.blit(start_phase.start_message, (start_phase.start_message_x, hover_offset_y))        
    
    elif game_phase == "gameplay":
        gameplay_phase.update()
        gameplay_phase.render(display)

        gameplay_phase.bird.draw(display)
        gameplay_phase.bird.update()

        if not any(pygame.key.get_pressed()):
            gameplay_phase.fall()
        
        ground_collision = pygame.sprite.groupcollide(ground_movement.ground, gameplay_phase.bird, False, False)
        pipe_collision = pygame.sprite.groupcollide(gameplay_phase.pipe_movement.pipe, gameplay_phase.bird, False, False)
        if ground_collision or pipe_collision:
            pygame.quit()
            
    pygame.display.update()
    clock.tick(60)
