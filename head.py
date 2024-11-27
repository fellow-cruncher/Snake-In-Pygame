from settings import *

class Head(pygame.sprite.Sprite):
    def __init__(self, time_then, time_interval, groups):
        super().__init__(groups)

        self.image = pygame.Surface(surfaces_size*0.9)
        self.image.fill(SNAKE_COLOR)
        
        self.rect = self.image.get_frect(center = offset)

        # time 
        self.time_interval = time_interval
        self.time_then = time_then
        
        # move
        self.move_distance = cell_size
        self.direction = pygame.Vector2(1,0)
        
    def input(self):
        keys = pygame.key.get_just_pressed()
        
        if keys[pygame.K_w]:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.x = 0
            self.direction.y = 1
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.direction.y = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.direction.y = 0
        
    def move(self):
        self.rect.center += (self.direction * self.move_distance)
        
    def does_collide(self, segment_list):
        if self.rect.centerx <= 0 or self.rect.centerx >= cell_number*34:
            return 1
        if self.rect.centery <= 0 or self.rect.centery >= cell_number*34:
            return 1
        
        for segment in segment_list:
            # * and exclude segment at index 1
            if self.rect.center == segment.rect.center and segment_list.index(segment) > 1:
                return 1
        
        return 0 
        
    def update(self):
        self.input()