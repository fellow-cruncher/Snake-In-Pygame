from settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self, head_rect, groups):
        super().__init__(groups)
        
        self.image = pygame.Surface(surfaces_size*0.9)
        self.image.fill(FOOD_COLOR)

        self.start_pos = self.randomize_position()
        self.rect = self.image.get_frect(center = self.start_pos)

        self.head_rect = head_rect
        
    def randomize_position(self):
        x_pos = randint(0, cell_number-1)*cell_size
        y_pos = randint(0, cell_number-1)*cell_size

        new_pos = pygame.Vector2(x_pos,y_pos) + offset
        
        return new_pos
