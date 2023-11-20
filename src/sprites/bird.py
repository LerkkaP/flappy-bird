import pygame
import os

dirname = os.path.dirname(__file__)

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = [pygame.image.load(os.path.join(dirname, "..", "assets/images/bird", f"bluebird-{i}.png")) for i in ["upflap", "midflap", "downflap"]]

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.velocity = 0  
        self.gravity = 0.2
        
    def update(self):
        
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.velocity < 0:
            self.image = pygame.transform.rotate(self.image, 30)
        else:
            self.gravity = 0.3
            self.image = pygame.transform.rotate(self.image, -40)
