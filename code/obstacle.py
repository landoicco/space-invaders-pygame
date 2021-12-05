import pygame


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../sprites/obstacles/meteor_big_brown_1.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
