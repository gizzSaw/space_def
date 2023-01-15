import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного приешельца"""
    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def draw(self):
        """класс одного приешельца"""   
        self.screen.blit(self.image, self.rect)
    def update(self):
        """перемещает пришельцев"""
        self.y += 0.2
        self.rect.y = self.y