import pygame
from sprites.bird import Bird
from start import Start

class Gameplay:
    def __init__(self, screen_width, screen_height):

        self.start_phase = Start(screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(self.screen_width / 3, self.screen_height / 2))


    def fly(self, dx=0, dy=0):
        for bird in self.bird.sprites():
            bird.rect.move_ip(dx, dy)

    def fall(self, dx=0, dy=4):
        for bird in self.bird.sprites():
            bird.rect.move_ip(dx, dy)

    

        