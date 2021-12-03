import pygame


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('sprites/meteor_brown_big2.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
