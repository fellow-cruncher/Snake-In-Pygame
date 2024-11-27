from settings import *

class Segment(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.image = pygame.Surface(surfaces_size*0.8)
        self.image.fill(SNAKE_COLOR)
        
        self.rect = self.image.get_frect(center = -offset)
        
    def move(self, destination):
        self.rect.center = destination
